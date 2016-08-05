@echo off&setlocal

:: Variables
set _BIN_DIR=%~dp0

:: Get project root dir
for %%i in ("%~dp0..") do set "_ROOT_DIR=%%~fi"

:: Get venv activate path
set _VENV_DIR=%_ROOT_DIR%\venv\ftrack-api-env\Scripts

:: Activate the venv and execute the launcher script
echo Launching Ftrack Connect...
cmd /k "cd /d %_VENV_DIR% & activate & cd /d %_BIN_DIR% & python launcher.py"

