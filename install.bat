@echo off 
set SRC=FreeCAD_Info
set DST=%APPDATA%\FreeCAD\Mod\FreeCAD_Info
echo "Copying %SRC% to %DST% ..."
robocopy /E %SRC% %DST%
pause
