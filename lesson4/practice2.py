def is_in_list_or_not(numbers:list, search_number:int):
    if search_number not in numbers:
        print('The number', search_number, 'is not searched at list')
    else:
        print('The number', search_number, 'is searched at list.')
        
numbers = [1, 3, 4, 5, 6, 8, 9, 11, 13, 14, 16, 17, 22, 24, 27, 55]
search_number = 16

# is_in_list_or_not(numbers, search_number)
# is_in_list_or_not(numbers, 7)

for index in range(30):
    is_in_list_or_not(numbers, index)
