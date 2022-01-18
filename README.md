# downloads-organizer
Python script to automatically arrange files in downloads folder based on rules

## setup
* put absolute path to `runner.bat` in `RunPythonScripts.vbs`, and path to `organizer.py` in `runner.bat`
* place `RunPythonScripts.vbs` in autostart folder
* modify `config.ini` to your needs, every rule is in regex format, name must be `ruleX` where X is number of the rule starting from 0, you also need to have associated folder with every rule
* now the script is run on startup and will be monitoring specified folder, and move each new file to appropriate folder
