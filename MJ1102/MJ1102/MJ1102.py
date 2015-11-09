from bs4 import BeautifulSoup
#xml 파싱
'''
f = open('test.xml')
xml = f.read()
soup = BeautifulSoup(xml)
for node in soup.findAll('node'):
    print("Node : "+node.string)
    print("Attr1 : "+node['attr1'])
f = open("song.xml",encoding = 'utf-8')
xml = f.read()
soup = BeautifulSoup(xml)
for nodes in soup.test('song'):
     print(nodes.find('title').string)
     print(nodes.find('length').string)

f = open("alcohol.xml",encoding="utf-8")
xml = f.read()
soup = BeautifulSoup(xml)
for nodes in soup.alcohol('cate1'):
    if nodes['tt'] == "안주":
        print(nodes['tt']+"-")
        for node in nodes('cate2'):
            print("\t"+node['tt']+"-")
            for item in node('item'):
                print("\t\t"+item.string)
'''
import json
data = {1:'a',2:'b'}
data2 = json.dumps(data)#파이썬 데이터를 json데이터로
data3 = json.loads(data2)#json데이터를 파이썬 데이터로
print(type(data2))#따라서 스트링
print(type(data3))#따라서 딕셔너리
data = {1:'우리',2:'나라'}
data2 = json.dumps(data,ensure_ascii=False)
print(data2)

s ="""
{
"name":"cybaek",
"detail":{"last":"baek"},
"emails":["cybaek@xxx.com","cybaek@yyy.com"]
}
"""
data = json.loads(s)
print(data['name'])
print(data['detail'])
print(data['detail']['last'])
class JsonObject:
    def __init__(self, d):
        self.__dict__ = d
data = json.loads(s, object_hook=JsonObject)
print(data.name)
print(data.detail)
print(data.detail.last)
for email in data.emails:
    print(email)