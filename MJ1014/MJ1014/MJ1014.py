import re
'''
pattern = re.compile("d")
result = pattern.search("dog")
print(result)
result = pattern.search("dog",1)
print(result)
p = re.compile('ab*')
print(p)
p = re.compile('ab*', re.IGNORECASE)
print(p)
p = re.compile(r'\section')
print(p)
p = re.compile(r'\\section')
print(p)

print(re.search("\\\\", "C:\\test"))
print(re.search(r"\\", "C:\\test"))

pattern = re.compile("o")
result = pattern.match("dog")
print(result)
result = pattern.match("dog",1)
print(result)
'''
str ='''sample1
sample2
sample3'''
'''
p = re.compile('^.*',re.S)
result = p.search(str)
print(result.group())

pattern = re.compile("o[gh]")
result = pattern.fullmatch("dog")
print(result)
result = pattern.fullmatch("ogre",0,2)
print(result.group())
result = pattern.fullmatch("doggie",1,3)
print(result.group())

pattern = re.compile("\W+")
result = pattern.split('words, words, words.')
print(result)
result = pattern.split('words, words, words.',1)
print(result)

pattern = re.compile("x*")
result = pattern.split('axbc')
print(result)

result = re.sub(r'\W','','a:b:c, d.')
print(result)

str= '<a href="index.html">HERE</a><font size="10">'
result = re.search(r'href="(.*?)">', str)
print(result.group(1))
'''
str = "123456-1234567"

pattern = re.compile("(\d{6})-(\d{7})")
result = pattern.fullmatch(str)
if result != None:
    pattern = re.compile("-")
    result = pattern.split(str)
    print(result)