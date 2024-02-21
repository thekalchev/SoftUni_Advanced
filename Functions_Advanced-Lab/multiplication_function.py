def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(1,4,5))