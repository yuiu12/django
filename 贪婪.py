import re
s = "<string>Weizhong Tu</string><string>Python is interestring</string>"
pattern = "<string>(.+?)</string>"  #括号代表里面的内容保存成子组
reg = re.compile(pattern)  #reg为regex对象
print(reg.findall(s))