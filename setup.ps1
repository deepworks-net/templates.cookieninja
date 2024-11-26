# Setup script for cookieninja environment
$ErrorActionPreference = "Stop"

# Create virtual environment
python -m venv .venv

# Activate virtual environment
& ".venv/Scripts/Activate.ps1"

# Upgrade pip and install required packages
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

Write-Host "Setup completed successfully!" -ForegroundColor Green