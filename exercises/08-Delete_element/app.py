people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    

     return list(filter(lambda x: x != person_name, people))
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))