"""
Testing for madlibs
"""
from .madlib import read_madlib_file, process_madlibs_template
import pytest


# test read_madlib_file


def test_read_madlib_file():
    """
    This tests the function that uses file_io's read_file to read the
    madlibs file
    """

    actual_filename = 'sample_template'
    expected_output = 'Hello {name}!\n'

    assert read_madlib_file(actual_filename)[1] == expected_output


def test_not_madlibs_file():
    """
    This tests the function that uses file_io's read_file to read the
    madlibs file, but uses a file that is not a madlibs file
    """

    actual_filename = 'sample'
    expected_output = 'The file was not a madlibs file!'

    assert read_madlib_file(actual_filename)[1] == expected_output


def test_madlib_read_exception():
    """
    This tests for read errors - i don't have any corrupt data to provide so
    I just tested for file not found
    """

    actual_filename = 'fasdfdafa'
    expected_output = 'File was not found!'

    assert read_madlib_file(actual_filename)[1] == expected_output



# test process_madlibs_template


# test for output string type
# test expected madlibs output vs actual (in true case)
# test that output doesn't match input (in true case)


#
