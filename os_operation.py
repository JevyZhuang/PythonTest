import os
path=os.getcwd()
print(os.getcwd())
print(os.path.abspath(path))
print(os.path.join(path,'A'))
print(os.path.exists("C\\demo"))