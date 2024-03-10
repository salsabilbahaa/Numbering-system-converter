# <<Numbering system converter>>

# Authors: Salsabil Bahaaeldin Rohaiem
#          Fatma Ali Abdelati Ali
#          Kenzy Hamdy Hassan Mohamed


# A function to check the validity of the input
def is_valid(number, base):
    number = number.upper()
    valid_digits = "0123456789ABCDEF"

    for digit in number:
        if digit not in valid_digits[:base]:
            return False
    return True

# Functions to convert from decimal base to other bases
def decimal_to_binary(num):
    num = int(num)
    binary_num = ""
    while num > 0:
        remainder = num % 2
        binary_num = str(remainder) + binary_num
        num //= 2
    return binary_num if binary_num else "0"

def decimal_to_octal(num):
    num = int(num)
    octal_num = ""
    while num > 0:
        remainder = num % 8
        octal_num = str(remainder) + octal_num
        num //= 8
    return octal_num if octal_num else "0"

def decimal_to_hexadecimal(num):
    num = int(num)
    hex_chars = "0123456789ABCDEF"
    hexadecimal_num = ""
    while num > 0:
        remainder = num % 16
        hexadecimal_num = hex_chars[remainder] + hexadecimal_num
        num //= 16
    return hexadecimal_num if hexadecimal_num else "0"

#Functions to convert from binary, octal, and hexadecimal bases to decimal base
def binary_to_decimal(num):
    num = str(num)
    decimal_num = 0
    power = 0
    for digit in num[::-1]:
        decimal_num += int(digit) * (2 ** power)
        power += 1
    return decimal_num

def octal_to_decimal(num):
    num = str(num)
    decimal_num = 0
    power = 0
    for digit in num[::-1]:
        decimal_num += int(digit) * (8 ** power)
        power += 1
    return decimal_num

def hexadecimal_to_decimal(num):
    num = str(num)
    hex_chars = "0123456789ABCDEF"
    decimal_num = 0
    power = 0
    for digit in num[::-1]:
        decimal_num += int(hex_chars.index(digit.upper())) * (16 ** power)
        power += 1
    return decimal_num

# A Function that converts between number system
def convert_number(number, initial_base, final_base):

    if initial_base.upper() == final_base.upper():
        return number #if the user wants to convert from decimal to decimal the output will be the same as the input number

    #if the user wants to convert from decimal to other numbering sustems
    elif initial_base.upper() == 'A':
        if final_base.upper() == 'B': number = decimal_to_binary(number)
        elif final_base.upper() == 'C': number = decimal_to_octal(number)
        elif final_base.upper() == 'D': number = decimal_to_hexadecimal(number)

    #if the user wants to convert from binary to other numbering sustems
    elif initial_base.upper()  == 'B':
        if final_base.upper() == 'A': number = binary_to_decimal(number)
        elif final_base.upper() == 'C':
            number = binary_to_decimal(number)
            number = decimal_to_octal(number)
        elif final_base.upper() == 'D':
            number = binary_to_decimal(number)
            number = decimal_to_hexadecimal(number)

    #if the user wants to convert from octal to other numbering sustems
    elif initial_base.upper()  == 'C':
        if final_base.upper() == 'A': number = octal_to_decimal(number)
        elif final_base.upper() == 'B':
            number = octal_to_decimal(number)
            number = decimal_to_binary(number)
        elif final_base.upper() == 'D':
            number = octal_to_decimal(number)
            number = decimal_to_hexadecimal(number)

    #if the user wants to convert from hexadecimal to other numbering sustems
    elif initial_base.upper()  == 'D':
        if final_base.upper() == 'A': number = hexadecimal_to_decimal(number)
        elif final_base.upper() == 'B':
            number = hexadecimal_to_decimal(number)
            number = decimal_to_binary(number)
        elif final_base.upper() == 'C':
            number = hexadecimal_to_decimal(number)
            number = decimal_to_octal(number)
    return number

while True:
    # The first menu that will appear to the user
    print("** numbering system converter **")
    print("A) Insert a new number")
    print("B) Exit program")

    menu1 = input("Please select an option (A/B): ")

    # if the user chose to insert a new number
    if menu1.upper() == 'A':
        number = input("Please insert a number: ")

        # A loop to check if the input contains a decimal point
        while True:
            if '.' in number:
                number = input("Error: float numbers are not allowed. Please enter a number without a decimal point: ")
            else:
                break

        # The second menu that will appear to the user
        print("** Please select the base you want to convert a number from **")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")

        initial_base = input("Please select an option (A/B/C/D): ")

        # Represent each base as a number
        if initial_base.upper() == 'A': base = 9
        elif initial_base.upper() == 'B': base = 2
        elif initial_base.upper() == 'C': base = 8
        elif initial_base.upper() == 'D': base = 16

        # A loop check if the entered number is valid in the chosen base
        while True:
            if is_valid(number, base) == False:
                number = input("Error: Please enter a valid number in the chosen base: ")
            else:
                break

        # The third menu that will appear to the user
        print("** Please select the base you want to convert a number to **")
        print("A) Decimal")
        print("B) Binary")
        print("C) Octal")
        print("D) Hexadecimal")

        final_base = input("Please select an option (A/B/C/D): ")

        result = convert_number(number, initial_base, final_base)

        if result is not None:
            print("Result:", result)

    # if the user wants to exit the program
    elif menu1.upper() == 'B':
        print("Exiting program. Goodbye!")
        break

    # if the user entered invalid choice
    else:
        print("Error: Invalid choice. Please enter a valid option.")