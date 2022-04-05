# ADTM_Tool
***A Python GUI tool to test ADTM.***   

## Dependencies:
python v3.10.2  
pyside6==6.2.4  
plotly==5.6.0  
pyinstaller==4.10 (optional)    
notice: pyinstaller is used for packing the python script file(\*.py) to executable file(\*.exe).  

## Dependencies install cmd:
```C
// install package with specified aliyun source path
pip install pyside6==6.2.4 -i https://mirrors.aliyun.com/pypi/simple
pip install plotly==5.6.0 -i https://mirrors.aliyun.com/pypi/simple
// or install all 
pip install requirements.txt
```

## Pack with pyinstaller
```C
pyinstaller -F --clean main.spec
//or  
pyinstaller -F -w --clean main.py
```
