from name_function import get_formatted_name

print('Enter q any time to quit')

while True:
    first = input('Enter your first name: ')
    if first == 'q':
        break
    last = input('Enter your last name: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)

    print(f"Neatly formatted name is {formatted_name}")