#different types of compound objects in Python

#Tuples which are the first type of compound objects, denoted by parantheses(),
#are sequences of different types of objects.
#Tuples can be summed up (resulting in concatanation) and an object inside a tuple can be a tuple itself.
#However, tuples can not be mutated so it is not possible to add an object to tuple or change one of it's objects

#The next type of compound objects is the list, denoted by square brackets ([]), 
#which has the same characteristics as that of the tuple with the different that it is mutable.

# The last type is called dictionary 
#which is a compound object the key values of which should not be sequence of integers 
#but it can accept any object as the key value.
#A dictionary is defined using curly braces {} using the following structure {'key':'value'}


#first type: tuple
t1=(1,2,3)
t2=("nome",3,6,"numero")
t3=t1+t2
t4=(t1,5,"noname",7)
t5=(t2,t3,t2,9)
#tuple cannot change just one element, we ve to change all the tuple
#second type: list, similar to tuple but the main difference is that u can do the mutation
L1=[1,2,3,4]

#struct: (el[0]:"type",el[1]:A,el[2]:L,el[3]:k)
R1=["conductive",2,.03,.9]

#now i introduce a new type: Dictionary
D1={"name":"R1","type":"conductive","area":1.2,"length":.03,"k":.9}


Reg1={"name":"Billy","surname":"Armstrong","birth":"200389","place":"London"}
Reg2={"name":"Alessandro","surname":"Zanetti","birth":"111192","place":"Milano"}
Reg3={"name":"Billy","surname":"Armstrong","birth":"200389","place":"London"}