@echo off
title CoinURL bot status
:start
del /f /s *.pyc
start /B /LOW /WAIT /AFFINITY 1 python coinurl.py
echo it crashed D:
goto start
