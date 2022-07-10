pcomp-1.3:
A simple library that calculates all possible permutations (with repetition) from an iterator and a length.

Functions:
valid_arguments:

Check if the arguments are valid.

Parameters:
    iterable (Iterable): The iterable object to be checked.
    length (int): The length to be checked.

Raises:
    TypeError: If iterable is not an Iterable or length is not an Integer or length is not greater than 0.

area:

Calculate the area for permutation computation.

Parameters:
    iterable (Iterable): The iterable object.
    length (int): The length for permutation computation.

Returns:
    int: The area for permutation computation.

pcomp:

Generate permutations of given iterable with specified length.

Parameters:
    iterable (Iterable): The iterable object.
    length (int): The length for permutation computation.

Returns:
    list: List of permutations of the given iterable with the specified length.

Example(hex to binnary):
Code:
import pcomp
print("Area:", pcomp.area(range(2), 4))  # it returns: 16
print("Permutations with repetition:", pcomp.pc(range(2), 4))  # it returns: [[0, 0, 0, 0], [0, 0, 0, 1], ..., [1, 1, 1, 1]]

The area function returns the total number of possible permutations with repetition.
And the pcomp function returns a list where each sublist represents one permutation.