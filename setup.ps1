<#
.SYNOPSIS
    Installs dependencies and synchronizes shared assets for local development.
#>
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

Push-Location -LiteralPath $PSScriptRoot

try {
    $requiredNode = [version]"22.13.0"

    $node = Get-Command node -ErrorAction SilentlyContinue
    if (-not $node) {
        throw "Node.js is not installed. Install Node.js $requiredNode or newer."
    }

    $currentNode = [version]((node -v).TrimStart("v") -replace "-.*$", "")
    if ($currentNode -lt $requiredNode) {
        throw "Node.js $requiredNode or newer is required, but $currentNode is active."
    }
    Write-Host "Node.js $currentNode detected."

    if (-not (Get-Command pnpm -ErrorAction SilentlyContinue)) {
        throw "pnpm is not installed. Run 'corepack enable pnpm' or 'npm install -g pnpm'."
    }
    Write-Host "pnpm $(pnpm --version) detected."

    # 'allowBuilds' in pnpm-workspace.yaml still holds placeholder values, so pnpm
    # refuses to finish the install. Downgrade that condition to a warning until the
    # entries are answered with 'pnpm approve-builds'.
    Write-Host "Installing dependencies..."
    pnpm --config.strict-dep-builds=false install
    if ($LASTEXITCODE -ne 0) {
        throw "Dependency installation failed."
    }

    Write-Host "Synchronizing shared resources into public web paths..."
    node tools/sync-public-assets.mjs
    if ($LASTEXITCODE -ne 0) {
        throw "Asset synchronization failed."
    }

    Write-Host ""
    Write-Host "Setup complete. Start the local site with:"
    Write-Host "  .\dev.ps1           Development server with hot reload"
    Write-Host "  .\dev.ps1 -Prod     Production build served locally"
}
finally {
    Pop-Location
}
