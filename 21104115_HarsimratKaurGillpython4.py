#>>>>>>>>>q1>>>>>>>>>

def tower_of_Hanoi(n ,a_pole,b_pole,c_pole):
#for 1 disc
    if n == 1:
        print("Move disc 1 from pole",a_pole,"to pole",c_pole)
        return
    tower_of_Hanoi(n-1,a_pole,c_pole,b_pole)
    print("Move disc",n,"from pole",a_pole,"to pole",b_pole)
    tower_of_Hanoi(n-1,c_pole,b_pole,a_pole)
n = 3
#calling
tower_of_Hanoi(n, 'A', 'C', 'B')
# A, B, C are the name of poles


#>>>>>>>.q2>>>>>>>>>

#recursion
n=int(input('Enter the number of rows:'))
def pascals_triangle(n,n1=n):
    if n==0:
        return
    pascals_triangle(n-1,n1)
#for spacing
    print(' '*(n1-n),end='')
    number=1
    for i in range(1,n+1):
        print(number,end=' ')
        number=number*(n-i)//i
    print()
pascals_triangle(n)

#Iteration
for j in range(1,n+1):
    print(' '*(n-j),end='')
    C=1
    for i in range(1,j+1):
        print(C,end=' ')

        C=C*(j-i)//i
    print()

#>>>>>>>.q3>>>>>>>>>

a=int(input('Enter a number in a:'))
b=int(input('Enter a number in b:'))
def func(x,y):
    divmod(x,y)
    return divmod(x,y)
x=func(a,b)
print(x)
#a
if  callable(func(a,b)) is  True:
    print('Yes')
else:
    print('No')
#b
if bool(0) not in x:
    print('All values are non zero')
else:
    print('All values are not non zero')
#c adding
y=x+(4,5,6)
print('Unfiltered:',y)
h=filter(lambda c:c<=4,y)
print('filtered:',tuple(h))
k=filter(lambda c:c<=4,y)
#d converting into set
d=set(k)
print(d)
#e making immutable
e=frozenset(d)
print(e)
#f maximum value in the set
print(max(e))
#hash value of the max value
print(hash(max(e)))

##>>>>>>>.q4>>>>>>>>>
class stu:
    def __init__(self , name , rollnumber):
        self.name = name
        self.rollnumber =rollnumber
    def func(self):
        print("Name is " ,self.name ," and Roll number is ", self.rollnumber)
    def __del__(self):
        print('deleted')
s1 = stu("Harsimrat", 21104115)
s1.func()

del s1
print('')

##>>>>>>>.q5>>>>>>>>>
class employee():
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def details(self):
        print(self.name,self.salary)

e1=employee('Mehak',40000)
e2=employee('Ashok',50000)
e3=employee('Viren',60000)

e1.details()
e2.details()
e3.details()
#a
e1.salary=70000
print('Updated salary of employee 1:')
e1.details()
del e3
print('Deleted the record of employee Viren')
print()

##>>>>>>>.q6>>>>>>>>>
from itertools import permutations
n=str(input('Enter the word uttered by George'))
m=str(input('Enter the word uttered by Barbie'))
for y in list(permutations(n)):
    z=''.join(y)
    if len(z)>2:
      print(z)
t=len(n)
s=len(m)
if t!=s:
  print('Your friendship is fake')


#to check if Barbie's word matches with any of the possible answers
if m in z:
    print('Your friendship is real')
else:
    print('Your friendship is fake')


























    







































    
