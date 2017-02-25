'''
#1
print('Single')
print("double")

#3
print(2 + 3)

#4

exampleVar = 55
print(exampleVar)
checkChar='hello'
print(checkChar)
canCon=5/4
print(canCon)

#5
x = 1
while x <= 10:
    print(x)
    x += 1

# did not run
con = 2

while con < 5:
    print('test %d  xxx' %con, con +1)
    con +=2

 #6
exlist = [1,4,3,6,5]
print(exlist)

for x in exlist:
    print(x)

for x in range(1,6):
    print('The value is %d' %x)

#7 8 9
x = 5
y = 5
z = 22

if x < y:
    #print('x < y')
    print('x - %d' %x ,'is less the y - %d' %y)
elif x==y:
    print('x = y')
else:
    print('x - %d' % x, 'is greater then y - %d' % y)

#10

def example():
    print('this code will be run')
    z = 3 + 4
    print(z)
example()

# 11
def simple_addition(num1, num2):
    answer = num1 + num2
    print(answer)
simple_addition(2,7)

def simple_substraction(num1, num2):
    answer = num1 - num2
    print(answer)
simple_addition(7,3)
simple_substraction(7,3)
simple_substraction(num2=7,num1=3)
'''

#12
def basic_window(width,height,font='TNR'):
    print(width,height,font)
basic_window(350,400)
basic_window(350,400,font='courier')