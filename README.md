# ADTM_Tool
***A Python GUI tool to test ADTM.***   

## Dependencies:
python v3.10.7  
pyside6==6.3.2  
plotly==5.10.0  
pyinstaller==5.4.1 (optional)  
notice: pyinstaller is used for packing the python script file(\*.py) to executable file(\*.exe).  

## Dependencies install cmd:
```C
// install package with specified aliyun source path
pip install pyside6==6.3.2 -i https://mirrors.aliyun.com/pypi/simple
pip install plotly==5.10.0 -i https://mirrors.aliyun.com/pypi/simple
pip install pyinstaller==5.4.1 -i https://mirrors.aliyun.com/pypi/simple
// or install all 
pip install requirements.txt
```

## Pack with pyinstaller
```C
pyinstaller --onefile --noconsole --clean -i ./resrc/icon/pycom.ico main.py
// or
pyinstaller --clean main.spec
```
