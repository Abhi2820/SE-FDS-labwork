Present= []
P= int(input ("No. of students who are present:"))
for i in range (0,P):
    a = int(input("Entre roll no:")) 
    Present.append(a)
z=len(Present)

    
x=int(input("Entre number that you want to search:"))


def sentinelSearch(Present, z, x):
 
    last = Present[z - 1]
    Present[z - 1] = x
    i = 0
 
    while (Present[i] != x):
        i += 1
 
    
    Present[z - 1] = last
 
    if ((i < z- 1) or (Present[z - 1] == x)):
        print(x, "has attended the training")
    else:
        print(x,"has not attended the training")
 
sentinelSearch(Present,z,x)
