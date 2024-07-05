a=[1,2,3]
b=[]
a.sort()
j=0
for i in range(1,len(a)):
	if a[j]==i:
		j=j+1
		continue
	else:
		b.append(i)
print(b[0])
