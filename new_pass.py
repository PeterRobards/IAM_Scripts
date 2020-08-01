#!/usr/bin/env python3
"""This script creates new passwords based on user provided parameters"""
# -*- coding: utf-8 -*-
# Copyright (c) 2020 Peter Robards
#
########################################################################################
#
# usage: NewPass.py [-h] [-l LENGTH] [-d DIGITS] [-s SPECIALS]
#
# optional arguments:
#  -h, --help            show this help message and exit
#  -l LENGTH, --length LENGTH
#                        password will be provided length. Default value = 16.
#  -d DIGITS, --digits DIGITS
#                        password will include provided number of digits
#  -s SPECIALS, --special_chars SPECIALS
#                        password will include provided number of special characters
#  -n NUMBER, --number_passwords NUMBER
#                        specify number of passwords to be generated
#
########################################################################################

import argparse
import secrets
import random
import string
import sys

# Method that converts a string to list and shuffle it to mix letters and digits
#  Depends on random library
def shuffle(sample_str):
    '''Converts a string to list and shuffle it to mix letters and digits'''
    sample_list = list(sample_str)
    random.shuffle(sample_list)
    final_string = ''.join(sample_list)
    return final_string

# Method to check for negative numbers
def check_length(num):
    """ Method to check for negative numbers - require sys library for sys.exit() method
        (catches scenarios where # digts and/or # special characters exceeds length of password)"""
    if num <= 0:
        # exits program if length is found to be 0 or less
        print("\nERROR -> password length cannot be:\t", num, "!")
        sys.exit("\nCheck specified password length, number of digts, & special characters.\n")

#### Define methods to create secure random passwords via the secrets library ####

# Default method: a mix of only upper and lowercase letters
def get_secure_random_string(length):
    """Return a mix of only upper and lowercase letters"""
    secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(length)))
    return secure_str

# Digits method: a mix of alphanumeric characters (A-Z,a-z,0-9)
def get_secure_random_string_digits(letter_count, digit_count):
    """Returna a mix of alphanumeric characters (A-Z,a-z,0-9)"""
    secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(letter_count)))
    secure_str += ''.join((secrets.choice(string.digits) for i in range(digit_count)))

    # Call shuffle() method to mix letters and digits
    secret = shuffle(secure_str)

    return secret

# Digits method: a mix of alphanumeric and special characters (A-Z,a-z,0-9,!-?)
def get_secure_random_string_punctuation(letter_count, digit_count, special_char_count):
    """Returna a mix of alphanumeric and special characters (A-Z,a-z,0-9,!-?)"""
    secure_str = ''.join((secrets.choice(string.ascii_letters) for i in range(letter_count)))
    secure_str += ''.join((secrets.choice(string.digits) for i in range(digit_count)))
    secure_str += ''.join((secrets.choice(string.punctuation) for i in range(special_char_count)))

    # Call shuffle() method to mix letters and digits
    secret = shuffle(secure_str)

    return secret


######################## Main Function ########################
def main():
    """Main Method: checks for user supplied args and generates password from supplied parameters"""

    #### Define optional command line arguments to tweak password settings via argparse library ####
    parser = argparse.ArgumentParser()

    parser.add_argument("-l", "--length", type=int, dest="length", default=16,
                    help="password will be provided length. Default value = 16.")
    parser.add_argument("-d", "--digits", type=int, dest="digits",
                    help="password will include provided number of digits")
    parser.add_argument("-s", "--special_chars", type=int, dest="specials",
                    help="password will include provided number of special characters")
    parser.add_argument("-n", "--number_passwords", type=int, dest="number", default=1,
                    help="specify number of passwords to be generated")
    ####

    # Initialize command line arguments
    args = parser.parse_args()

    # assign password length using either default value or user provided argument
    length = args.length
    # assign number of passwords to create using either default value or user provided argument
    num_pass = args.number

    print("\n***** Generating Password(s)... *****\n")

    # Check if Special Characters have been requested
    if args.specials:
        specials=args.specials
        # Check if Digits have also been requested
        if args.digits:
            digits = args.digits
            spec_length = length-digits-specials
            check_length(spec_length)
            print("\nPassword(s):")
            for i in range(num_pass):
                print("\n\t", get_secure_random_string_punctuation(spec_length, digits, specials))
        else:
            digits=0
            spec_length = length-digits-specials
            check_length(spec_length)
            print("\nPassword(s):")
            for i in range(num_pass):
                print("\n{}.)\t{}"
                .format(i,get_secure_random_string_punctuation(spec_length, digits, specials)))

    # Check if Digits have been requested
    elif args.digits:
        digits = args.digits
        dig_length = length-digits
        check_length(dig_length)

        print("\nPassword(s):")
        for i in range(num_pass):
            print("\n\t", get_secure_random_string_digits(dig_length, digits))

    # Use Default password settings
    else:
        print("\nPassword(s):")
        for i in range(num_pass):
            print("\n\t", get_secure_random_string(length))

    print("\n")


######################## Driver Code ########################
if __name__ == '__main__' :

    # Call main function
    main()
