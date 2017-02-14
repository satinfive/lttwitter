@echo off
setlocal

:: utf8.bat infile outfile
:: convert infile to utf8 and save as outfile

if not exist "%~1" goto usage
if "%~2"=="" goto usage

set "infile=%~f1"
set "outfile=%~f2"

:: store current console codepage to var
for /f "tokens=2 delims=:" %%I in ('chcp') do set "_codepage=%%I"

:: temporarily change console codepage to UTF-8
>NUL chcp 65001

:: set byte order mark for outfile
>"%outfile%" set /p "=﻿" <NUL

:: dump infile to outfile encoded as UTF-8
>>"%outfile%" type "%infile%"

:: restore console to original codepage
>NUL chcp %_codepage%

goto :EOF

:usage
echo Usage: %~nx0 infile outfile