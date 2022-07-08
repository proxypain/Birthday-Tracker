bdays = {"tre": "march 21", "mom": "november 19th", "dad": "june 14th"}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    
    if name in bdays:
        print(bdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday info for ' + name)
        print('What is their birthday?')
        bday = input()
        bdays[name] = bday
        print('Birthday database updated.')
