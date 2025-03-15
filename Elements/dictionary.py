#JAI SHREE RAM

D={}
D1={1:'Apple',2:'Banana',3:'Cherry'}
D2={'name_1':'Ajay','name_2':'Vjay','name_3':'Sharma'}
D3={1:'Circle','pi':'3.14','r':'5'}

print(D)
print(D1)
print(D2)
print(D3)

#Using the  dict() function
D4=dict(w='parrot',x='tiger',y='lion',z='peacock')
print(f'\n{D4}')

#Acccessing the element from the dictionary
print(D2['name_3'])
print(D2.get('name_1'))

#Adding an element to the dictionary
D2['age']=25
print(D2)

#Updating the value of the dictionary
D2['name_3']='Verma'
print(D2)

#Deleting an element from the dictionary
del D1[1]         #using del keyword
print(D1)

val=D2.pop('name_2')    #using pop() function
print(D2)
print(val)

k, v= D3.popitem()    #
print(f'kay={k}, value={v}')
print(D3)

D1.clear()  #using clear function
print(D1)
