"""Tests for file_io.py"""


from .file_io import read_file, write_file
import pytest


def test_read_file():
    """Testing read_file for successful file read"""
    filename = 'sample'
    assert read_file(filename) == 'hello!\n'


def test_read_no_file():
    """Test read_file for file couldn't be found"""
    filename = 'asdf'
    with pytest.raises(FileNotFoundError):
        read_file(filename)


def test_read_type_error():
    """Test read_file for wrong input type"""
    filename = {}
    with pytest.raises(TypeError):
        read_file(filename)


def test_write_file():
    """Testing write_file for successful write by writing then reading"""
    filename = 'test'
    content = 'hello!'

    write_file(content, filename)
    assert read_file(filename) == 'hello!'


def test_incorrect_input():
    """Testing write_file for incorrect input"""
    content = 'hi'
    filename = {}

    with pytest.raises(TypeError):
        write_file(content, filename)

    content = {}
    filename = 'hi'

    with pytest.raises(TypeError):
        write_file(content, filename)
