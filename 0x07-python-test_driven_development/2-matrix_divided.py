#!/usr/bin/python3
"""
This module contains the definition of an
addition function.

"""


def matrix_divided(matrix, div):
    """Divides all element of a matrix """
    # Validate matrix type
    if type(matrix) is not list:
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    
    for row in matrix:
        if type(row) is not list:
            raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
        if len(matrix[0]) != len(row):
            raise TypeError('Each row of the matrix must have the same size') 
    
    # Validte div type
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    
    new_matrix = [row[:] for row in matrix]
    return [ [round(elem / div, 2) for elem in row]  for row in new_matrix ]
