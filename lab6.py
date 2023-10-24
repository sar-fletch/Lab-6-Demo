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
            password = input("Enter you 8 digit password to encode:")
            new_pass = encode(password)
            print(new_pass)

        elif choice == '2':
            pass        # to do decode function

        elif choice == '3':
            break




