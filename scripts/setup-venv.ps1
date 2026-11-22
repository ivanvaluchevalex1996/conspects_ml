# Создаёт .venv в корне репозитория и ставит зависимости из requirements.txt
$ErrorActionPreference = "Stop"
$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
Set-Location $RepoRoot

function Find-Python312 {
    $candidates = @(
        @{ Exe = "py"; Args = @("-3.12", "-c", "import sys; print(sys.executable)") },
        @{ Exe = "python"; Args = @("-c", "import sys; print(sys.executable)") }
    )
    foreach ($c in $candidates) {
        try {
            $out = & $c.Exe @c.Args 2>$null
            if ($LASTEXITCODE -eq 0 -and $out -match "3\.12") { return $out.Trim() }
        } catch { }
    }
    throw "Нужен Python 3.12 (py -3.12 или python в PATH). См. README."
}

$python = Find-Python312
Write-Host "Python: $python"

if (-not (Test-Path ".\.venv\Scripts\python.exe")) {
    & $python -m venv .venv
}

& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\pip.exe install -r requirements.txt

Write-Host ""
Write-Host "Готово. В Cursor интерпретатор уже в .vscode/settings.json (относительный путь к .venv)."