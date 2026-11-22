# Один раз на компьютер: Python 3.12 + все пакеты из requirements.txt (не .venv)
$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$Req = Join-Path $RepoRoot "requirements.txt"

function Find-Python312 {
    if (Get-Command py -ErrorAction SilentlyContinue) {
        $v = & py -3.12 -c "import sys; print(sys.executable)" 2>$null
        if ($LASTEXITCODE -eq 0) { return $v.Trim() }
    }
    $default = Join-Path $env:LOCALAPPDATA "Programs\Python\Python312\python.exe"
    if (Test-Path $default) { return $default }
    throw "Нет Python 3.12. Скачай с https://www.python.org/downloads/ (галочка Add to PATH)."
}

$python = Find-Python312
Write-Host "Используем: $python"
& $python -m pip install --upgrade pip
& $python -m pip install -r $Req
Write-Host ""
Write-Host "Готово. В Cursor: интерпретатор ${env:LOCALAPPDATA}\Programs\Python\Python312\python.exe"
Write-Host "Папку .venv в проекте можно удалить — она не нужна."