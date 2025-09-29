a=int(input())
def num(a):
     c=[]
     for i in range(1,a+1):
              c.append(i)
     return (c)
print(num(a))




a=[ [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
c=c+a[0]
c=c+a[1][3]+a[2][3]+a[3][3]+a[3][2]+a[3][1]+a[3][0]+a[2][0]+a[1][0]+a[1][1]+a[1][2]+a[2][2]+a[2][1])
print(c)









a=input()
c=[]
d=[]
f=len(a)
for i in range(len(a)//2):
    c.append(a[i])
    d.append(a[f-i-1])
s=0
b=0
for i in range (len(c)):
    s=s+int(c[i])
    b=b+int(d[i])
if b== s:
    print(b)
else:
    print('no')















a=[]
while True:
    print("\n1.əlavə et\n2.dəyiş\n3.sil\n4.göstər")
    b=input("seçim:")
    if b=="1":
        a.append(input("ad:"))
    elif b=="2":
        c=(input("köhnə ad"))
        if c in a:
            a[a.index(c)]=input("yeni ad")
    elif b=="3":
        d=input("silinəcək ad")
        if d in b:
            b.remove(d)
    elif b== "4":
        if len(a)!=0:
            print(a)
        else:
            print("boşdur")                    
            
    
    
