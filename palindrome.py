#!/usr/bin/python3
#Palindrome: Write a program to check if a given string is a palindrome (a word, phrase, number, or other sequence of characters which reads the same backward as forward).
def is_palindrome(s):
    return s[::-1]
    
    
string =input("enter the string: ")
print("the palindrome",is_palindrome(string))
    

    
