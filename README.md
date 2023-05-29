# ADTM_Tool
***A Python GUI tool to test ADTM.***   

## Dependencies:
python v3.11.2  
pyside6  plotly  pyinstaller(optional)  
notice: pyinstaller is used for packing the python script file(\*.py) to executable file(\*.exe).  

## Dependencies install cmd:
```C
// install package with specified tsinghua source path
pip install pyside6==6.5.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install plotly==5.14.1 -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install pyinstaller==5.11.0 -i https://pypi.tuna.tsinghua.edu.cn/simple  (optional)
// or install all 
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Pack with pyinstaller
```C
pyinstaller --onefile --noconsole --clean -i ./resrc/icon/adtm.ico main.py
// or
pyinstaller --clean main.spec
```
