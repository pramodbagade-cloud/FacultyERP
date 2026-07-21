@echo off
title FacultyERP Version Tag

echo ==========================================
echo      Create Git Version Tag
echo ==========================================
echo.

set /p version=Enter Version (Example v0.4.0):

set /p message=Enter Tag Message:

git tag -a %version% -m "%message%"

git push origin %version%

echo.
echo Tag Created Successfully.
pause