

def square_sum(numbers):
    
    result = 0
    
    for num in numbers:
        result += num**2
        
    return result

ret = square_sum([1, 2, 2])
print(ret)