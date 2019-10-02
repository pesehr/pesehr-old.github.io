'''
Program name: Worksheet05
Program description: Develop a program that convert numbers in different bases complete #todo
'''

input_base = input("Please enter the base of the input number (b:binary, d:decimal, o:octal, h:hexadecimal c:char) :")

output_base = input("Please enter the base of the output number (b:binary, d:decimal, o:octal, h:hexadecimal c:char) :")

number = input("Please enter the number:")

if input_base == output_base:
    print(number)
else:

    # convert string to  decimal number
    if input_base == 'b':
        number = int(number, 2)
    elif input_base == 'o':
        number = int(number, 8)
    elif input_base == 'd':
        number = int(number, 10)
    elif input_base == 'h':
        number = int(number, 16)
    elif input_base == 'c':
        number = ord(number)

     # print the number in requested base
    if output_base == 'b':
        print(bin(number))
    elif output_base == 'o':
        print(oct(number))
    elif output_base == 'd':
        print(number)
    elif output_base == 'h':
        print(hex(number))
    elif output_base == 'c':
        print(chr(number))
