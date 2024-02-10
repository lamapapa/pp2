#1

    def calculate_factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * calculate_factorial(n - 1)

#2
    def reverse_string(input_str):
        return input_str[::-1]
    
#3
    def getmax(a, b, c):
        return max(a, b, c)
    
#4
    def is_even(num):
        return num % 2 == 0

#5
    def word_frequency(input_str):
    words = input_str.split()
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

#6
    def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#7
    def calculate_running_average(numbers):
    total = 0
    averages = []
    for i, num in enumerate(numbers):
        total += num
        averages.append(total / (i + 1))
    return averages

#8 classes & objects
    
    class MyShape:
    def __init__(self, color="default_color", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        return f"Color: {self.color}, Filled: {self.is_filled}"

    def get_area(self):
        return 0
#9
    class Rectangle(MyShape):
    def __init__(self, color="default_color", is_filled=False, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def __str__(self):
        return f"{super().__str__()}, Top Left: ({self.x_top_left}, {self.y_top_left}), Length: {self.length}, Width: {self.width}"

    def get_area(self):
        return self.length * self.width

#10
    import math

class Circle(MyShape):
    def __init__(self, color="default_color", is_filled=False, x_center=0, y_center=0, radius=0):
        super().__init__(color, is_filled)
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius

    def __str__(self):
        return f"{super().__str__()}, Center: ({self.x_center}, {self.y_center}), Radius: {self.radius}"

    def get_area(self):
        return math.pi * self.radius**2

#11 rectangle
    # Example usage
color = input("Enter color for Rectangle: ")
is_filled = input("Is it filled? (True/False): ")
x_top_left = float(input("Enter x-coordinate of the top-left corner: "))
y_top_left = float(input("Enter y-coordinate of the top-left corner: "))
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))           

my_rectangle = Rectangle(color, is_filled, x_top_left, y_top_left, length, width)
print(my_rectangle)
print(f"Area: {my_rectangle.get_area()}") 

    
def print_triangle(height):
    for i in range(1, height + 1):
        print('*' * i)

print_triangle(10)




