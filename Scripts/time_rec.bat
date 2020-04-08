@echo off
title Counting time
set /p t=Coding time? 
set /p c=Do what? 
echo --------------------------------->>time_rec.txt
echo %DATE%%TIME% 学习了%t%h %c% >>time_rec.txt
pause
