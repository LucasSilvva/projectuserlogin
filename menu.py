
def Menu()-> None:
    from main import User
    while True:
        print('MENU')
        print('1 - Register ')
        print('2 - Login ')
        print('3 - Exit ')
        try:
            choice_user = int(input('Choose an option: '))
            if choice_user == 1:
                print('\n--- Register ---')
                name = input('Name: ')
                email = input('Email: ')
                password = input('Password: ')
                user = User(nome, email, password)
                user.Register()
            
            if choice_user == 2:
                print('\n--- Login ---')
                email = input('Email: ')
                password = input('Password: ')
                user = User(name="", email=email, password=password) 
                user.Login()
            if choice_user == 3:
                print('Exiting the system. Goodbye!')
                break
                
        except ValueError:
            print('Invalid Input.')


