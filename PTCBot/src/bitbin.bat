@echo off
title BitBin bot status
:start
del /f /s *.pyc
start /B /LOW /WAIT /AFFINITY 1 python bitbin.py
echo it crashed D:
goto start
