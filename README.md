# ADTM_Tool
***A Python GUI tool to test ADTM.***   

## Dependencies:
```C
python v3.11.5
pyside6
plotly
```

## Dependencies install cmd:
```C
// install package with specified tsinghua source path
pip install pyside6==6.5.2 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install plotly==5.16.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
// or install all 
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Pack with pyinstaller
```C
// install pyinstaller  
pip install pyinstaller==5.13.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
// generate exe
pyinstaller --onefile --noconsole --clean -i ./resrc/icon/adtm.ico adtm.py
```
