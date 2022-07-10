from collections.abc import Iterable

def valid_arguments(iterable,length):
    """
    Check if the arguments are valid.

    Parameters:
        iterable (Iterable): The iterable object to be checked.
        length (int): The length to be checked.

    Raises:
        TypeError: If iterable is not an Iterable or length is not an Integer or length is not greater than 0.
    """
    if not(isinstance(iterable, Iterable)):
        raise TypeError("Iterable Argument is not Iterable")
    if not(isinstance(length, int)):
        raise TypeError("Length Argument is not Integer")
    if not(length>0):
        raise TypeError("Length Argument must be >0")


def area(iterable,length):
    """
    Calculate the area for permutation computation.

    Parameters:
        iterable (Iterable): The iterable object.
        length (int): The length for permutation computation.

    Returns:
        int: The area for permutation computation.
    """
    valid_arguments(iterable,length)
    result = len(iterable)**length

    return result


def pc(iterable,length):
    """
    Generate permutations of given iterable with specified length.

    Parameters:
        iterable (Iterable): The iterable object.
        length (int): The length for permutation computation.

    Returns:
        list: List of permutations of the given iterable with the specified length.
    """
    power = area(iterable,length)
    temp_list = [[None]*length for i in range(power)]

    negative_index = range(-1,-length-1,-1)

    for i in negative_index: # row (right to left)
        change = pow(len(iterable),abs(i+1)) # Calculate the frequency of change based on current row position
        index = 0

        for j in range(power): # column
            if j % change == 0 and j!=0: # Check if it's time to change the index based on the change frequency
                index = (index + 1) % len(iterable) # Update the index for the iterable
            temp_list[j][i] = iterable[index]

    result = temp_list

    return result