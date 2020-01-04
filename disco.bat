@echo off
Setlocal EnableDelayedExpansion
cls
set "string=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
set "colors=0123456789ABCDEF"

set "blob=`"

TIMEOUT /T 4

:top

set /a num=%random% %% 16
color !colors:~%num%,2!

set /a x=%random% %% 62
set blah=!string:~%x%,1!
set "blob=%blob%%blah%"
echo %blob%

goto top

ping -n 1 google.com  | find "Reply" > nul