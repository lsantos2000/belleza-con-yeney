<#
.SYNOPSIS
    Runs the YeneyWellness site locally.
.EXAMPLE
    .\dev.ps1
    Starts the development server with hot reload.
.EXAMPLE
    .\dev.ps1 -Prod -Port 4000
    Builds for production and serves the result on port 4000.
#>
[CmdletBinding()]
param(
    [ValidateRange(1, 65535)]
    [int]$Port = 3000,

    [switch]$Prod
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

Push-Location -LiteralPath $PSScriptRoot

try {
    if (-not (Test-Path -LiteralPath "node_modules")) {
        throw "Dependencies are missing. Run .\setup.ps1 first."
    }

    $vinext = "node_modules/vinext/dist/cli.js"

    Write-Host "Synchronizing shared resources into public web paths..."
    node tools/sync-public-assets.mjs
    if ($LASTEXITCODE -ne 0) {
        throw "Asset synchronization failed."
    }

    Write-Host ""
    Write-Host "Spanish home: http://localhost:$Port/"
    Write-Host "English home: http://localhost:$Port/en"
    Write-Host ""

    if ($Prod) {
        Write-Host "Building for production..."
        node $vinext build
        if ($LASTEXITCODE -ne 0) {
            throw "The production build failed."
        }

        Write-Host "Starting the production server on port $Port..."
        node $vinext start -p $Port
    }
    else {
        Write-Host "Starting the development server on port $Port..."
        node $vinext dev -p $Port
    }
}
finally {
    Pop-Location
}
