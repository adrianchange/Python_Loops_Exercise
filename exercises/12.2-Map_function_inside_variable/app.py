names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']

def prepender(name):
    return f"My name is: {name}"
#Your code go here:
new_list = list(map(prepender, names))
print(new_list)