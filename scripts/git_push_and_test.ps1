param(
    [string]$CommitMessage = "chore(ui): unify module templates, add module_base and placeholders"
)

Write-Host "Staging changes..."
git add -A

Write-Host "Committing..."
git commit -m $CommitMessage

Write-Host "Pushing to origin/develop..."
git push origin develop

Write-Host "Installing requirements into venv (if present)..."
if (Test-Path -Path .\.venv\Scripts\python.exe) {
    .\.venv\Scripts\python.exe -m pip install -r requirements.txt
    Write-Host "Running Django tests..."
    .\.venv\Scripts\python.exe manage.py test --verbosity 2
} else {
    Write-Warning "Virtualenv not found at .\.venv. Activate your venv and run tests manually."
}

Write-Host "Done. If any step failed, inspect the output above." 
