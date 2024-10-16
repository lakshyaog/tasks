def range_bitwise_and(left, right):
    shift = 0
    #Find the common prefix of left and right
    while left < right:
        left >>= 1
        right >>= 1
        shift += 1
     
    return left << shift


test_cases = [
    (5, 7),      # Output 4
    (0, 0),      # Output 0
    (1, 2147483647)  # Output0
] 


for left, right in test_cases:
    print(range_bitwise_and(left, right))

# TIME COMPLEXCITY:
print("time complexcity will be O(logn) ")