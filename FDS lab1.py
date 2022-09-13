'''

In second year computer engineering class, group A student’s play cricket, group B students
play badminton and group C students play football.
Write a Python program using functions to compute following: 
a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton

'''

cricket = []
n_A = int(input ("No. of students who play cricket:"))
for i in range (0,n_A):
    a = str(input("Entre name of student:")) 
    cricket.append(a)

print("________________________________________________________________________________________")

football= []
n_B = int(input ("No. of students who play football:"))
for i in range (0,n_B):
    b= str(input("Entre name of student:")) 
    football.append(b)

print("__________________________________________________________________________________________")
badminton= []
n_C= int(input ("No. of students who play badminton:"))
for i in range (0,n_C):
    c = str(input("Entre name of student:")) 
    badminton.append(c)


print("__________________________________________________________________________________________")
print("A =",cricket)
print("B =",football)
print("C =",badminton)
print("__________________________________________________________________________________________")



def minus (lst1, lst2):
    lst = []
    for i in lst1:
        if i not in lst2:
            lst.append(i)
   
    return lst

def intersection (lis1, lis2):
    lst = []
    for i in lis1:
        if i in lis2:
            lst.append(i)
    return lst

def union (lst1, lst2):
    lst = lst1.copy()
    for i in lst2:
        if i not in lst:
            lst.append(i)
    return lst

def unionall (lst1, lst2, lst3):
    lst = lst1.copy()
    for i in lst2:
        if i not in lst:
            lst.append(i)
    for i in lst3:
        if i not in lst:
            lst.append(i)
    return lst

print ("Students playing both cricket and badminton : ",union(cricket, badminton))
print("__________________________________________________________________________________________")

CuB = union(cricket,badminton)
Cib = intersection(cricket,badminton)
result1 = minus(CuB,Cib)
print ("Students playing cricket or badminton : ",result1)
print("__________________________________________________________________________________________")


U = unionall(cricket, badminton, football)
result2 = minus(U,CuB)
print ("No. of students playing Nither cricket Not badminton :",len(result2))
print (result2)
print("__________________________________________________________________________________________")


result3= minus(U, badminton)
print ("No. of students playing cricket and football not badminton :",len(result3))
print(result3)
print("__________________________________________________________________________________________")
