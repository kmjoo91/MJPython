import re
#그룹화
str = '''Window
Unix
Linux
Solaris'''
p = re.compile('^.+', re.M)
print(p.findall(str))
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)",
"Malcolm Reynolds")
print(m.group('first_name', 'last_name'))
print(m.groups())
m = re.match(r"(\d+)\.?(\d+)?", "24d1")
print(m.groups())
print(m.groups(0))
#그룹 딕셔너리
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)",
"Malcolm Reynolds")
print(m.groupdict())

#특정문자열까지만
p = re.compile(".+:")
m = p.search("http://google.com")
print(m.group())
p = re.compile(".+(?=:)")
m = p.search("http://google.com")
print(m.group())

import os
os.chdir("C:\\")
currentpath = os.getcwd()
print(currentpath)
import glob
l = glob.glob("*")
print(l)
p = re.compile('.*[.](?!bat$|exe$).*$')
for item in l:
    if p.match(item):
        print(item)

#문자열 찾기
p = re.compile("(?<=abc)def")
m = p.search("abcdef")
print(m.group())
#문자열 start() end()
email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
result = email[:m.start()] + email[m.end():]
print(result)

#포커
'''
valid = re.compile(r"^[a2-9tjqk]{5}$")
displaymatch(valid.match("akt5q"))
displaymatch(valid.match("akt5e"))
displaymatch(valid.match("akt"))
displaymatch(valid.match("727ak"))
'''
#전화번호부
text = """Ross: McFluff: 834.345.1254: 155 Elm Street
Ronald: Heathmore: 892.345.3428 436: Finley Avenue
Frank: Burger: 925.541.7625 662: South Dogwood Way
Heather: Albrecht: 548.326.4584 919: Park Place"""
entries = re.split("\n", text)
result = [re.split(":?", entry, 4) for entry in entries]
print(result)

import urllib.request

with urllib.request.urlopen("http://www.naver.com") as f:
    txt = repr(f.read())
    title_start = re.search("<title>",txt)
    title_end = re.search("</title_>",txt)
    title = txt[title_start.end():title_end.start()]
    print(title)