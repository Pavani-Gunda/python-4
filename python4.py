#arthimetic operations
 #opeations using numbers
#integers
print(94+73)
print(94-73)
print(94*73)
print(94/73)
print(94**7)
print(94//73)


#using variables
num1 = 75
num2 = 25
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)
print(num1//num2)


#strings
print("good-evening")
print("glad to see you")
hello= "glad to see you"
print(hello)
print(len(hello))
print(type(hello))

#index 
time= "if you cant find a way, create one!"
print(time)
print(len(time))
print(time[2])
print(time[16])
print(time[17])

#slicing
text= " difficulties in life are intended to make us better, not bitter"
print(text)
print(len(text))
print(text[1: 17])
print(text[2: 6: 2])
print(text[5: 9:-3])
print(text[1:1])
print(text[ :14])
print(text[24: ])
print(text[-5 : -15: -2])
print(text[ : : -2])
print(text[-1:-64])
print(id(text))#to know the address
print("index 17 value is", text[17])
#text[17]= 't' 
#print(text[17]) # immutability
print(type(15))#int
print(type(23.89))#float

#complex numbers
a= 6+5j
b= 5+8j
print(type(a))
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
#print(a//b) #unsupported

#modules
print(63/2)
print(63//2)
print(63%2)


#booleans---- TRUE OR FALSE
  

pin = 7890
print(pin == 7890)
print(68>87)
print(35>=35)
  
username = "kani%16"
pin = 7890
if username == pin:
    print("success")
if True:
    print("success")
print(int(True))# value


#list

list1 = [1, 2, 3, "strings1", True, [9,56, 34]]
print(list1)
print(len(list1))
print(type(list1))
print(list1[5])
print(list1[5][1])
print(list1[1: 6])
print(list1[1:1])
print(list1[ : ])
print(list1[-6: -9])
print(list[3: 5: 9])
list1[5][1]= "hello world"
print(list1)   #list is changed beacause list is mutable
variables=  list1
print(list1)


#TUPLE
tuple= [3, 9, 6.5, [6, 5, 7], "animals"]
print(tuple)
print(tuple[4])
print(tuple[3][2])
print(tuple[-2])
print(len(tuple))

#range
print(list(range(0, 200)))
print(list(range(0, 200, 2)))
print(list(range(0, 200, 1)))
print(list(range(200, 0, -1)))
print(list(range(200, 0, -2)))


list_1 = [1, 22, 36, 99]
for i in list_1:
    print(i)

#dicitonary

dict = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven'}
print(dict)
print(len(dict))
print(id(dict))
dict[3] = 'eight'  #mutable
print(dict)
dict['2'] = 'nine'
print(dict)
dict['10'] = 'ten'
print(dict)
dict['10'] = 'eleven'
print(dict)
 


 #set
set = {2, 3, 5, 66, "day", "night"}
print(set)
print(set)


#none
num= None
print(num)
print(type(num))


#input

 #input("number1")
 #print(input("number1"))
a= input("number")
print(input("number"))
b= input("other numer")
print(input("other number"))
print(a+b)
