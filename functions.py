def menu()-> None:
    while True:
        print('MENU')
        print('1 - Register ')
        print('2 - Login ')
        print('3 - Exit ')
    try:
        choice_user = int(input('Choose an option: '))
        

    except ValueError:
        print('Invalid Input.')


