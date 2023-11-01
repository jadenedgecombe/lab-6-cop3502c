# Jaden Edgecombe

# Encoded Function
def encode(info):
    new_value = ""
    for num in info:
        if int(num) + 3 == 10:
            new_value += "0"
        elif int(num) + 3 == 11:
            new_value += "1"
        elif int(num) + 3 == 12:
            new_value += "2"
        else:
            new_value += str(int(num) + 3)

    return new_value


# Main Function
def main():
    password = ""
    encoded_password = ""

    active = True
    while active:
        print("Menu")
        print("------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit\n")

        user_option = int(input("Please enter an option: "))

        if user_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        elif user_option == 2:
            print("The encoded password is " + encoded_password + ", and the original password is " + password + ".\n")
        elif user_option == 3:
            active = False


if __name__ == "__main__":
    main()
