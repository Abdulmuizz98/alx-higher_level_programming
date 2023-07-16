#!/usr/bin/python3
"""Module to multiply 2 matrices
"""


def matrix_mul(m_a, m_b):
    """Multiplies 2 matrices
    """
    # Type Validation
    # m_a, m_b must be a list
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')

    # m_a, m_b must be a list of lists
    for el in m_a:
        if type(el) is not list:
            raise TypeError('m_a must be a list of lists')
    for el in m_b:
        if type(el) is not list:
            raise TypeError('m_b must be a list of lists')

    # Value validation
    # m_a, m_b can't be empty list
    if m_a == [] or m_a == [[]]:
        raise ValueError('m_a can\'t be empty')
    if m_b == [] or m_b == [[]]:
        raise ValueError('m_b can\'t be empty')

    # Type Validation
    # m_a, m_b must be a list of lists which containing ints or floats
    for el in m_a:
        for i in el:
            if type(i) not in [int, float]:
                raise TypeError('m_a should contain only integers or flaots')
        if len(m_a[0]) != len(el):
            raise TypeError('each row of m_a must be of the same size')

    for el in m_b:
        for i in el:
            if type(i) not in [int, float]:
                raise TypeError('m_b should contain only integers or flaots')
        if len(m_b[0]) != len(el):
            raise TypeError('each row of m_b must be of the same size')

    # Value Validation
    # Cant be multiplied if number of col in A is not equal to number
    # of rows in B
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')

    # Get to work
    # row, col of new matrix; then mul reps the equal col and row of 2 matrices
    res_row, res_col, res_mul = len(m_a), len(m_b[0]), len(m_b)
    res_matrix = [[0 for i in range(res_col)] for i in range(res_row)]

    i = 0
    while i < res_row:
        j = 0
        while j < res_col:
            sum = 0
            k = 0
            while k < res_mul:
                sum += m_a[i][k] * m_b[k][j]
                k += 1
            res_matrix[i][j] = sum
            j += 1
        i += 1

    return res_matrix
