SOURCE_FILE = __file__


def double_eights(n):
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    pre = n % 10
    def inner(pre,n):
        if(n < 10):
            return False
        if(pre == 8):
            next = n//10%10
            if(next == 8):
                return True
            else:
                return inner(next,n//10)
        else:
            return inner(n//10%10,n//10)
    return inner(pre,n)    

def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    if(b == 0):
        return a
    return gcd(b,a%b)


def pascal(row, column):
    """Returns the value of the item in Pascal's Triangle
    whose position is specified by row and column.
    >>> pascal(0, 0)    # The top left (the point of the triangle)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 3 (1 3 3 1), Column 2
    3
    >>> pascal(4, 2)     # Row 4 (1 4 6 4 1), Column 2
    6
    """

    if column > row:       # 外面
        return 0
    if column == 0 or column == row:  # 边界
        return 1
    return pascal(row-1, column-1) + pascal(row-1, column)

    


def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    if(m == 1):
        return 1
    if(n == 1):
        return 1
    return paths(m-1,n)+paths(m,n-1)

