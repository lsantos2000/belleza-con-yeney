[CmdletBinding()]
param(
    [Parameter(Position = 0)]
    [ValidateNotNullOrEmpty()]
    [string]$Message = "Update website",

    [ValidateNotNullOrEmpty()]
    [string]$Remote = "github"
)

$ErrorActionPreference = "Stop"
Set-StrictMode -Version Latest

Push-Location -LiteralPath $PSScriptRoot

try {
    git rev-parse --is-inside-work-tree *> $null
    if ($LASTEXITCODE -ne 0) {
        throw "This script must be run from a Git repository."
    }

    $branch = (git branch --show-current).Trim()
    if (-not $branch) {
        throw "Git is in detached HEAD state. Check out a branch before running this script."
    }

    $changes = git status --porcelain
    if (-not $changes) {
        Write-Host "No changes to commit."
        exit 0
    }

    git add --all
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to stage the changes."
    }

    git commit -m $Message
    if ($LASTEXITCODE -ne 0) {
        throw "Unable to create the commit."
    }

    $gitHubToken = $null
    if (Get-Command gh -ErrorAction SilentlyContinue) {
        $gitHubToken = (& gh auth token 2>$null)
        if ($gitHubToken) {
            $gitHubToken = $gitHubToken.Trim()
        }
    }

    if ($gitHubToken) {
        $credential = [Convert]::ToBase64String(
            [Text.Encoding]::ASCII.GetBytes("x-access-token:$gitHubToken")
        )
        git -c "http.https://github.com/.extraheader=AUTHORIZATION: basic $credential" push $Remote $branch
    }
    else {
        git push $Remote $branch
    }
    if ($LASTEXITCODE -ne 0) {
        throw "The commit was created, but the push to '$Remote/$branch' failed."
    }

    Write-Host "Committed and pushed '$branch' to '$Remote'."
}
finally {
    Pop-Location
}
