# Approch for this code:
def generate_pascal_triangle(n):# define a class called generate_pascale_triangle:
    triangle = []
    
    for i in range(n):#use nested for loop for the implementation of the pascale:
        row = [0] * (i + 1) 
        row[0] = 1  
        row[i] = 1  
        
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)

    return triangle

if __name__ == "__main__":#used condiional statement for the num to taken as 5:
    n = 5
    pascal_triangle = generate_pascal_triangle(n)
    
    for row in pascal_triangle:
        print(row)


# THE TIME COMPLEXCITY OF THIS CODE BY BIG (O) NOTATION 
# BY looping we for the time complexcity 
print("O(n)*2: time complexcity of this code")