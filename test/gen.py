import random

def generate_good_password(length):
    # 1 set alphabet
    alphabet =  'abcdefghijklmnopqrstuvwxyz'\
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
                '0123456789!@#%^&*()_-+?><,.{}'

    #return ''.join(random.choices(alphabet, k=length))

    # 2 get random symbol
    # 3 repeat (2) length times 
    # 4 join all symbols to string
    password = ''
    for i in range(length):
        password += random.choice(alphabet)

    return password

for i in range(10):
    print(generate_good_password())
