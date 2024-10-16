def number_spiral(y, x):
    
    layer = max(abs(y), abs(x))
    
    
    max_num = (2 * layer + 1) ** 2
    
    
    if y == layer:
        #Bottom row
        return max_num - (layer - x)
    elif x == -layer:
        #Left column
        return max_num - (2 * layer) - (layer - y)
    elif y == -layer:
        #Top row
        return max_num - (2 * layer) - (layer + x)
    elif x == layer:
        #Right column
        return max_num - (3 * layer) + (layer + y)


test_cases = [
    (2, 3),  # Output: 8
    (1, 1),  # Output: 1
    (4, 2),  # Output: 15
]


for y, x in test_cases:
    print(number_spiral(y, x))
# time coplexcity:
print("time complexcity for the code will be O(n):")