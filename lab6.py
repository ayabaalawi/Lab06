#name: aya ba alawi

def encoder(password):
    res = ''
    for digit in str(password):
        encoded_pass = int(digit) + 3
        if len(str(encoded_pass)) >= 2:
            encoded_pass =  encoded_pass - 10
        res += str(encoded_pass) #concentating the string
    return res

# Lucca Carvalho Magalhaes
def decoder(password):
    decoded = ""
    for i in password:
        decoded += str((int(i) - 3) % 10) 
    return decoded

def main():
    program_running = True
    while program_running:
        print('\nMenu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')

        menu_option = int(input('\nPlease enter an option: '))
        if menu_option == 1:
            user_password = input('Please enter your password to encode: ')
            user_password = encoder(user_password)
            print('Your password has been encoded and stored!')

        elif menu_option == 2:
            print(f'The encoded password is {user_password}, and the original password is {decoder(user_password)}.')

        elif menu_option == 3:
            program_running = False


if __name__ == '__main__':
    main()
