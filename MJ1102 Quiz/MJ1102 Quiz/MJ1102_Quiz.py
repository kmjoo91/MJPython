import re

pattern1 = re.compile("(.{7})(.)")
pattern2 = re.compile(".{13}")
pattern3 = re.compile("[a-zA-Z]")
pattern4 = re.compile("[0-9]")
pattern5 = re.compile("[^a-zA-Z0-9]")
pw1 = "11a1111%ddd33333"
result1 = pattern1.search(pw1)
result2 = pattern2.search(pw1)
result3 = pattern3.search(pw1)
result4 = pattern4.search(pw1)
result5 = pattern5.search(pw1)
print(result2)
try:
    t = result1.group(2)
    if result2 =="None":
        if result3 =="None":
            if result4 =="None":
                if result5 =="None":
                    print("하잇!")
except:
    print("바잇")