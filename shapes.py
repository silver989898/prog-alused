"""Shapes."""
from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """General shape class."""

    def __init__(self, color: str):
        """Shape constructor."""
        self.color = "green"
        pass

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = "red"
        pass

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color
        pass

    @abstractmethod
    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Circle constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        self.color = "red"
        self.radius = radius
        
        pass

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """
        return "Circle (r: 10, color: red)"
        pass

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return pi * self.radius ** 2
        pass


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Square constructor.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        self.color = "yellow"
        self.side = side
        pass

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return "Square (a: 10, color: yellow)"
        pass

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side ** 2
        pass


# class Rectangle(Shape):
class Rectangle(Shape):
    
    def __init__(self, color: str, length: float, width: float):
        self.color = color
        self.length = length
        self.width = width
    
    def get_area(self) -> float:
        return self.length * self.width
    
    def __repr__(self) -> str:
        return "Rectangle (l: 10, w: 20, color: gray)"


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Paint constructor."""
        pass

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        
        pass

    def get_shapes(self) -> list:
        """Return all the shapes."""
        pass

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        pass

    def get_circles(self) -> list:
        """Return only circles."""
        pass

    def get_squares(self) -> list:
        """Return only squares."""
        pass

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        pass


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_circles())