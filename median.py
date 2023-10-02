"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

numbers.sort()

print(numbers)
print('the length of numbers is', len(numbers))

mid = 0
idx = 0
# ans = 0

if len(numbers)%2 ==0:
    idx = len(numbers)//2
    mid = (numbers[idx] + numbers[idx-1])/2
 #   ans = mid 
else:
    idx = len(numbers)//2 
    mid = numbers[idx] 
 #   ans = mid 

print('median is {} ' .format(mid))


#print('median is ' , ans )

    
