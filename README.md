# ADTM_Tool
***A Python GUI tool to test ADTM.***   

## Steps to run the tool
```C
// install uv tool in windows powershell:
irm https://astral.sh/uv/install.ps1 | iex
// set up environment with below cmd on ADTM_Tool path:
uv sync
// run the python file
uv run python main.py
```

## Package into ADTM.exe with pyinstaller
```C
// install pyinstaller  
uv pip install pyinstaller
// generate exe
pyinstaller -D -w --clean --add-data "data/*:data" -i ./resrc/icon/adtm.ico main.py -n ADTM
// run the executable file: ADTM.exe
```
