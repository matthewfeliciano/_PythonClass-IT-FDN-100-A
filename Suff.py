input("Enter your name: ")

x = int(input('enter x value: '))


'''
Created on Apr 15, 2016

@author: feliciam
'''
'''
exampleList = [1,6,7,3,6,9,0]

for thing in exampleList:
    print(thing)


for x in range(1,11):
    print(x)
'''

'''
# if statements
x = 2
y = 7
z = 10

if x > y:
    print(x, 'is greater than', y) 

if x < y:
    print(x, 'is less than', y) 

if x == y:
    print (x, 'is the same as', y)

#cannot do this
#if x < '2':
#    print(x, 'is less than 2')

if x <= y:
    print(x, 'is less than or equal to', y)

if z > y > x:
    print(z, 'is greater than',y,'which is greater than',2)
'''

'''
# if else statements
x = 13
y = 6

if x < y:
    print (x, 'is less than',y)

if x > y:
    print  (x,'is greater than',y)
else:
    print (x, 'is not less than',y)
'''

'''
#If Elif Else Statements

x = 3
y = 7
z= 10


if x < y and x < z:
    print ('something here was the case')
elif x < z:
    print(x,'is less than',z)
elif y < z:
    print (y,'is less than',z)
else:
    print ('nothing was the case')
    
'''

#Functions 05/06/16
'''
def example ():
    x = 1
    y = 3
    print(x+y)  

    if x < y:
        print(x, 'is less than', y)
example()
'''
#Function Parameters 05/06/16
'''
def addition (num1,num2,num3,num4):
    answer = num1+num2+num3+num4
    return answer

x = addition(5,6,6,5)
print (x)
'''
'''
def website (font='TNR',
              background_color='white',
              font_size='11',
              font_color='black'):
    print('font:',font)
    print('bg:',background_color)
    print('Font size:',font_size)
    print('Font color:',font_color)
    

#website('TNR','white','11','black')

#website(font_color='black',
#       font='TNR',
#      background_color ='white',
#     font_size ='11',)

website(background_color='grey')
'''

'''
#Global and Local Variables 05/06/16

x = 6

def example3():
    global x
    x += 1
    print(x)
example3()


def example():
    z = 5
    print(z)

# cannot do this:    
#print(z)
    
def example2():
    z = 7
    print(z)  
    y = x + 1
    print(y)
    return y
x = example2()

print(x)
'''

#Common Python Errors 05/06/16

#print('starting here')

#NameError:
'''
#variable = 55
#print(variable)
'''

#Expected an indent:

'''def func1():
      
def func2():
    print(2)
'''

# Unexpected Indent:
'''
def task():
   print('1')
   
print('2')

    print('3')
'''

print('Hey there how are you today?')
