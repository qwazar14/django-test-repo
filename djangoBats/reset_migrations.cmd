@echo off
set /P var="Enter app name: "
call python ../manage.py migrate --fake "%var%" zero
call python ../manage.py showmigrations
call makemigrat+migration.cmd
