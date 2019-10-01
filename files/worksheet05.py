'''
Program name: Worksheet05
Program description: Develop a program that convert numbers in different bases.
Use oct() bin() hex() chr() ord() and int() to complete the following code
'''

input_base = input("Please enter the base of the input number (b:binary, d:decimal, o:octal, h:hexadecimal, c:char) :")

output_base = input("Please enter the base of the output number (b:binary, d:decimal, o:octal, h:hexadecimal, c:char) :")

number = input("Please enter the number:")

if input_base == output_base:
    print(number)
else:

    # convert string to  decimal number
    if input_base == 'b':
        number = int(number, 2)
    elif input_base == 'o':
        #TODO
    elif input_base == 'd':
        #TODO
    elif input_base == 'h':
        #TODO
    elif input_base == 'c':
        #TODO

     # print the number in requested base
    if output_base == 'b':
        #TODO
    elif output_base == 'o':
        #TODO
    elif output_base == 'd':
        #TODO
    elif output_base == 'h':
        #TODO
    elif output_base == 'c':
        #TODO
