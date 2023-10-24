# Sara Fletcher
#10 / 23 /23


def encode(password):
    string = str(password)
    encoded_pass = ''

    for digit in string:
        if int(digit) <= 6:
            num = str(int(digit) + 3)
            encoded_pass += num
        elif int(digit) == 7:
            num = '0'
            encoded_pass += num
        elif int(digit) == 8:
            num ='1'
            encoded_pass += num
        elif int(digit) == 9:
            num = '2'
            encoded_pass += num
    return encoded_pass



def decode(new_pass):
    pass   #  partner to do












# Sara Fletcher
# 10/23/23

if __name__=='__main__':
    print("Menu")
    print("-----------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()


    while True:
        choice = input('Please choose a menu option: ')

        if choice == "1":
            password = input("Please enter you 8 digit password to encode:")
            new_pass = encode(password)
            print(' Your password has been encoded and stored')

        elif choice == '2':
            print(f' Your encoded password is {new_pass} and the original password is {decode(new_pass)}')

        elif choice == '3':
            break




