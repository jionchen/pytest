#!/usr/bin/env python
 
def is_happy_number(num):
    seen = [4,16,37,58,89,145,42,20]
    while True:
        sum_digits = sum(int(digit) ** 2 for digit in str(num))
        if sum_digits == 1:
            return True
        elif sum_digits in seen:
            return False
        else:
            num = sum_digits
 
if __name__ == '__main__':
 
    happies = [] # list of happy numbers found
 
    num = int(raw_input("input a number:"))
 
    for i in range(1,num+1):
        if is_happy_number(i):
            happies.append(i)
         
 
    print happies
