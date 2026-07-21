@echo off
title FacultyERP GitHub Push

echo ==========================================
echo        FacultyERP GitHub Backup
echo ==========================================
echo.

echo Current Status
git status

echo.
echo ==========================================
echo Adding all modified files...
echo ==========================================
git add .

echo.
set /p msg=Enter Commit Message:

echo.
echo ==========================================
echo Creating Commit...
echo ==========================================
git commit -m "%msg%"

echo.
echo ==========================================
echo Pushing to GitHub...
echo ==========================================
git push origin main

echo.
echo ==========================================
echo Current Tags
echo ==========================================
git tag

echo.
echo Done.
pause