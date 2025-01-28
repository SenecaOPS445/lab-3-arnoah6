#!/usr/bin/env python3 


'''Lab 3 part 1 Script - functions'''

#Author ID: 129556221

def sum_numbers(number1, number2):
   return int(number1 + number2)

def subtract_numbers(number1, number2):
    return int(number1 - number2)

def multiply_numbers(number1, number2):
    return int(number1 * number2)

if __name__=='__main__':
    print(sum_numbers(10, 5))
    print(subtract_numbers(10, 5))
    print(multiply_numbers(10, 5))
