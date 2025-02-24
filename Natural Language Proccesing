#Natural Language Processing(NLP)
n=int(input())
tc=0
sc=0
l=[]
for j in range(n):
    L=input()
    if len(L)>0:
        l.append(L[0:100])
    else:
        print("Invalid Input")
for i in l:
    for j in i:
        if j=='s' or j=='S':
            sc+=1
        elif j=='t' or j=='T':
            tc+=1
if tc>sc:
    print('English')
else:
    print("French")