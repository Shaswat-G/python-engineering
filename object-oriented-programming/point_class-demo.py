class Point:
    default_color = "red"  # Class variable
    default_size = 10      # Class variable
    
    def __init__(self, x, y): # Constructor method
        self.x = x      # Instance variable
        self.y = y
      
    def __str__(self):  # String representation method, redefines the behavior of str() and print()
        return f"({self.x}, {self.y})"
    
    def __eq__(self, other):  # Equality method, redefines the behavior of == operator
        if not isinstance(other, Point):  # Check if other is an instance of Point
            return NotImplemented
        return self.x == other.x and self.y == other.y
        
    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) > (other.x, other.y)
    
    def __add__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return Point(self.x + other.x, self.y + other.y)
    
    @classmethod # decorator
    def zero(cls): # Class method
        return cls(0, 0)
        
        
        
    def draw(self):
        print(f"Point ({self.x}, {self.y})")
        


Point.default_color = "blue"  # Changing class variable
print(Point.default_color)  # Accessing class variable  
point = Point(1,2)
print(point.x)
print(point.y)
print(point.default_color)  # Accessing class variable through instance
point.draw()
print(type(point))
print(isinstance(point, Point))

origin = Point.zero()  # Using class method to create an instance
print(origin.x, origin.y)  # Output: 0 0    
print(origin)
print(str(origin))  # Output: (0, 0)

print(point == origin)  # Output: False
print(point > origin)  # Output: True
print(point < origin)  # Output: False  Python automatically understands what lt means after defining gt
print(point != origin)  # Output: True  Python automaticallyunderstands what != meands after defining lt

print(point + origin)  # Output: (1, 2)  Python automatically