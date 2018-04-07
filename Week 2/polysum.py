from math import tan,pi

def polysum(n, s):
    """
    Input: Given n sides and the s length of each side
    n positive integer
    s positive int or float
    Output:
    Returns the sum of the area and the square of the perimeter of the regular polygon, rounded to 4 decimal places.
    """
    sum = (0.25*n*(s*s)) / tan(pi/n)
    sum += (n*s)**2
    
    return round(sum, 4)
