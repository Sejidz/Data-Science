@echo off
echo Running datacleaning-ratings.py
python datacleaning-ratings.py
echo.
echo Running datacleaning-crashes.py
python datacleaning-crashes.py
echo.
echo Running datacleaning-sales.py
python datacleaning-sales.py
echo.
echo All scripts executed.
echo will open dashboard after pressing any key
pause
python model.py