e=[]
d=[]
f=open("eng-de.txt","r")
for i in f:
    s=i.replace("\n","").split("-")
    e.append(s[0])
    d.append(s[len(s)-1])
f.close()
e.pop(0)
d.pop(0)
w=input()
f=open("history.txt","a")
f.write(f"{w}\n")
f.close()
b=False
for i in range(len(e)):
    if e[i] == w:
        b=True
        print(f"{d[i]}")
        break
if b == False:
    print("Not Found")