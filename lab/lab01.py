def add():
    """
    add(1, 5) -> return 6
    add(10, 3) -> return 13
    """

def subtract():
    """
    subtract(1, 5) -> -4
    subtract(10, 3) -> 7
    """

def mul():
    """
    mul(1, 5) -> 5
    mul(10, 3) -> 30
    """

def square():
    """
    square(1) -> 1
    square(5) -> 25
    """

def sum_squares():
    """
    Return a^2 + b^2. Can you use methods defined above?
    sum_squares(1, 5) -> 26
    sum_squares(10, 3) -> 109
    """

def min():
    """
    Return the lower of the two numbers.
    min(1, 5) -> 1
    min(10, 3) -> 3
    """

def max():
    """
    Return the higher of the two numbers.
    max(1, 5) -> 5
    min(10, 3) -> 3
    """

def abs_value():
    """
    Return the absolute value of a number.
    abs_value(1) -> 1
    abs_value(-1) -> 1
    """

# Do not change anything below this line.
def main():
    print("Checking functionality of Add")
    assert(sum(1, 5), 5)
    assert(sum(10, 3), 13)
    print("Checking functionality of Subtract")
    assert(sub(1, 5), -4)
    assert(sub(10, 3), 7)
    print("Checking functionality of Mul")
    assert(mul(1, 5), 5)
    assert(mul(10, 3), 30)
    print("Checking functionality of Square")
    assert(square(1), 1)
    assert(square(5), 25)
    print("Checking functionality of Sum_squares")
    assert(sum_squares(1, 5), 26)
    assert(sum_squares(10, 3), 109)
    print("Checking functionality of min")
    assert(min(1, 5), 1)
    assert(min(10, 3), 10)
    print("Checking functionality of max")
    assert(max(1, 5), 5)
    assert(max(10, 3), 10)
    print("Checking functionality of abs_value")
    assert(abs_value(1), 1)
    assert(abs_value(-1), 1)
