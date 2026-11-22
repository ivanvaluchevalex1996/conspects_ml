# Расширения из .vscode/extensions.json (после установки Cursor)
$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$Json = Get-Content (Join-Path $RepoRoot ".vscode\extensions.json") -Raw | ConvertFrom-Json

if (-not (Get-Command cursor -ErrorAction SilentlyContinue)) {
    throw "CLI cursor не в PATH. Открой Cursor → Command Palette → Shell Command: Install 'cursor' command in PATH."
}

foreach ($id in $Json.recommendations) {
    Write-Host "Installing $id ..."
    cursor --install-extension $id --force
}
Write-Host "Готово. Reload Window в Cursor."