"""Functions for reading/writing files"""


def read_file(filename):
    """
    Reads file and returns output

    input: string, a filename to be opened
    output: string, the file contents
    """

    if type(filename) is not str:
        raise TypeError('filename must be a string')

    with open('./' + filename + '.txt') as f:
        return f.read()

    try:
        with open(filename + '.txt') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError('Your file was not found')
    except IOError:
        raise IOError('There was an error reading your file')


def write_file(content, filename):
    """
    Receives input, writes to new txt file

    input:
        content: string, to be written
        filename: filename to be written to
    output: string, confirmation
    """

    if type(content) is not str or type(filename) is not str:
        raise TypeError('You must enter valid content and filename')

    try:
        with open('./' + filename + '.txt', 'w') as f:
            f.write(content)
            return ('success')
    except IOError:
        return('fail')


if __name__ == "__main__":
    print(read_file('empty'))
