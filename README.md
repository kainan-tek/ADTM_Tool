# ADTM_Tool
***A Python GUI tool to test ADTM.***   

## Dependencies:
python v3.10.4  
pyside6==6.3.0  
plotly==5.7.0  
pyinstaller==5.0 (optional)  
notice: pyinstaller is used for packing the python script file(\*.py) to executable file(\*.exe).  

## Dependencies install cmd:
```C
// install package with specified aliyun source path
pip install pyside6==6.3.0 -i https://mirrors.aliyun.com/pypi/simple
pip install plotly==5.7.0 -i https://mirrors.aliyun.com/pypi/simple
// or install all 
pip install requirements.txt
```

## Pack with pyinstaller
```C
pyinstaller --clean main.spec
//or  
pyinstaller --onefile --noconsole --clean main.py
```
