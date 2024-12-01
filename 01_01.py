with open('input1.txt','r') as file:
#with open('input1-test.txt','r') as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

a=[]
b=[]
linetot=0
for line in lines:
    a.append(int(line.split()[0]))
    b.append(int(line.split()[1]))

#print(a)
a.sort()
b.sort()

dsum = 0
for i,val in enumerate(a):
    t = abs(a[i]-b[i])
    dsum+=t

print(dsum)
