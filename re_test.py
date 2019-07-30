import re

txt = "1925年牛顿被苹果砸到头后发现了万有引力。"
ans = re.search("^1925年", txt)
print(ans)

ans = re.search("[1-2][0-9]{3}", txt)
print(ans)

ans = re.findall(r"\d+年", txt)
print(ans)

url = "http://www.baidu.com?p=111&password=123"
ans = re.findall("www..+.com", url)
print(ans)

mail = "-------mailzhon@163.com-----"
ans = re.findall("[a-z]+@\d+.com", mail)
print(ans)

name = "232048289zhong zi hao 322802"
ans = re.findall("[a-z]+\s[a-z]+\s[a-z]+", name)
print(ans)

phone = "2004-984-994 # 这是一个电话号码"
num = re.sub(r"#.*$", "", phone)
print(num)

num = re.sub(r"\D", "", phone)
print(num)

pattern = re.compile(r"\d+")
m = pattern.match("one12twothree34four", 3)
print(m)
