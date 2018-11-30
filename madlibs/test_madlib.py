"""
Testing for madlibs
"""

from madlibs import madlib, file_io
import pytest


# test read_madlib_file


def test_read_madlib_file():
    """
    This tests the function that uses file_io's read_file to read the
    madlibs file
    """

    actual_filename = 'sample_template'
    expected_output = 'Hello {name}!\n'

    assert madlib.read_madlib_file(actual_filename)[1] == expected_output


def test_not_madlibs_file():
    """
    This tests the function that uses file_io's read_file to read the
    madlibs file, but uses a file that is not a madlibs file
    """

    actual_filename = 'sample'
    expected_output = 'The file was not a madlibs file!'

    assert madlib.read_madlib_file(actual_filename)[1] == expected_output


def test_madlib_read_exception():
    """
    This tests for read errors - i don't have any corrupt data to provide so
    I just tested for file not found
    """

    actual_filename = 'fasdfdafa'
    expected_output = 'File was not found!'

    assert madlib.read_madlib_file(actual_filename)[1] == expected_output


# prompt_user_filename


def test_filename_input_match():
    """
    This tests whether what the user inputs matches the output of the function
    """
    def mock_input(s):
        return 'foobar'
    madlib.input = mock_input
    assert madlib.prompt_user_filename() == 'foobar'


# process_madlibs_template


def test_if_template():
    """
    This tests with a file that is a proper template to make sure it is
    processed correctly.
    """
    madlibs_template = [True, 'Hello {name}']

    def mock_input(s):
        return 'foobar'
    madlib.input = mock_input
    assert madlib.process_madlibs_template(madlibs_template) == [True, 'Hello foobar']


def test_if_not_template():
    """
    This tests with a file that is not a proper template to make sure there
    is a rejection.
    """
    madlibs_template = [False, 'Hello lunch']

    assert madlib.process_madlibs_template(madlibs_template) == [False, 'Hello lunch']


# prompt_for_words


def test_prompt_for_words_output():
    """
    This tests the output of the function when the proper input has been
    provided
    """
    def mock_input(s):
        return 'foobar'

    madlib.input = mock_input
    input_words = ['Adjective']

    assert madlib.prompt_for_words(input_words) == ['foobar']


# output_to_user


def test_output_save():
    """
    This tests whether the file is written and output to a file
    """
    user_input = iter(['y', 'filename'])

    def mock_input(s):
        return next(user_input)

    madlib.input = mock_input

    madlib.output_to_user([True, 'Completed madlib'])

    assert file_io.read_file('filename') == 'Completed madlib'


def test_no_save():
    """
    This tests whether the madlib is saved when it's not requested to be saved.
    """
    user_input = iter(['n', 'another_filename'])

    def mock_input(s):
        return next(user_input)

    madlib.input = mock_input

    madlib.output_to_user([True, 'Completed madlib'])

    with pytest.raises(FileNotFoundError):
        file_io.read_file('another_filename')
