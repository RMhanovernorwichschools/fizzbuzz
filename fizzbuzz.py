"""
fizzbuzz.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write a program that prints the numbers from 1 to 100. But for 
multiples of three print “Fizz” instead of the number and for 
the multiples of five print “Buzz”. For numbers which are multiples 
of both three and five print “FizzBuzz”.

We will use a variation of this test in which the last number of 
the series isn't necessarily 100, and the two numbers being tested 
for multiples aren't necessarily three and five. For example, your 
program should behave just like this:

How many numbers shall we print? 25
For multiples of what number shall we print 'Fizz'? 3
For multiples of what number shall we print 'Buzz'? 5
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
"""
max=int(input('How many numbers shall we print? '))
numbers=[n+1 for n in range(0,max)]

ft=int(input("For multiples of what number shall we print 'Fizz'? "))
bt=int(input("For multiples of what number shall we print 'Buzz'? "))
for n in numbers:
    if n/ft==int(n/ft) and n/bt==int(n/bt):
        print('FizzBuzz')
    elif n/ft==int(n/ft) and n/bt!=int(n/bt):
        print('Fizz')
    elif n/bt==int(n/bt) and n/ft!=int(n/ft):
        print('Buzz')
    else:
        print(n)