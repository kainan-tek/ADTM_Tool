# ADTM_Tool
***A Python GUI tool to test ADTM.***   

## Dependencies:
python v3.10.2  
pyside6==6.2.2.1  
plotly==5.5.0  
pyinstaller==4.8 (optional)    
notice: pyinstaller is used for packing the python script file(\*.py) to executable file(\*.exe).  

## Dependencies install cmd:
```C
pip install pyside6==6.2.2.1
// install with specified source
pip install plotly==5.5.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
// install all 
pip install requirements.txt
```

## Pack with pyinstaller
```C
pyinstaller -F --clean main.spec  
//or  
pyinstaller -F --clean main.py
```
