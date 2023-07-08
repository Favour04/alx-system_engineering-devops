#!/usr/bin/python3
"""
    This module is
    contain the func
    find_peak that is
    defined to find
    the peak in a li-
    st of number
"""


def find_peak(list_of_numbers):
    if len(list_of_numbers) == 0:
        return None
    else:
        peak = sorted(list_of_numbers)
        return peak[-1]
