#!/usr/bin/python
__author__= 'OG'

# Pads a string with trailing spaces so length equals a mulitple of 16 Bytes

def add_spaces(s, num):
    for n in range(need_to_add):
        s += " "
    print("New string is: ", s)
    print("Length = ", get_string_length(s) )

def get_string_length(s):
    return len(s.encode('utf-8'))

go = True
while go:
    s = input("Enter a string: ")
    b_size = get_string_length(s)
    if b_size < 16:
        need_to_add = 16 - b_size
        add_spaces(s, need_to_add)

    elif b_size % 16 != 0:
        over_byte = b_size % 16
        need_to_add = 16 - over_byte
        add_spaces(s, need_to_add)

    else:
        print("String is: ", s)

    again = input("Do another? ")
    if again == "n":
        go = False
