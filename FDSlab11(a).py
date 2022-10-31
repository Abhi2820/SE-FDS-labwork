Present= []
P= int(input ("No. of students who are present:"))
for i in range (0,P):
    a = int(input("Entre roll no:")) 
    Present.append(a)
z=len(Present)

    
x=int(input("Entre number that you want to search:"))
def linearSearch(Present, z, x):

    for i in range(0, z):
        if (Present[i] == x):
            return i
    return -1




result = linearSearch(Present, z, x)
if(result == -1):
    print("Student has not attended the training")
else:
    print("Student has attended the training")
