def hello():
    print('Hello')

def hello2(name, age):
    year = 2020 - age
    print('Hello', name, 'Your year of birth:', year)
    print('Hello '+name, 'Your year of birth:', year)

hello()
hello2('Nick', 25)
