"""Madlibs! Open in the command line to play"""


from file_io import read_file, write_file
from textwrap import dedent
# import re
import sys


def greet_user_prompt():
    """
    This greets the user when they first start

    No input/output
    """

    ln_1 = 'Welcome to madlibs!!'
    ln_2 = 'To play, enter the file name of a madlibs file (no extension).'
    ln_3 = 'You\'ll then be prompted for words. When done, you\'ll receive'
    ln_4 = 'your completed madlibs and be able to save.'
    ln_5 = 'To exit at any time, type "quit"'

    print(dedent(f'''
    {'*' * 80}

    {'{:^80}'.format(ln_1)}

    {'{:^80}'.format(ln_2)}
    {'{:^80}'.format(ln_3)}
    {'{:^80}'.format(ln_4)}

    {'{:^80}'.format(ln_5)}

    {'*' * 80}
    '''))


def read_madlib_file():
    """
    This takes the user's input, asks file_io to read the file,
    returns a list with the success/fail status of read, and content (or error
    message)

    No input
    output: list, bool fail/pass + madlibs template/error message
    """
    filename = input('Your madlibs file (no extension): ')
    try:
        content = read_file(filename)
        if '{' in content:
            return [True, content]

        return [False, 'The file was not a madlibs file!']
    except FileNotFoundError:
        return [False, 'File was not found!']
    except IOError:
        return [False, 'Error reading your file!']
    except Exception:
        return [False, 'Unknown error! Try again!']




def process_madlibs_template(madlibs_template):
    """
    This takes in a madlibs template as a string

    input: list:
        bool, fail/pass of read
        string, madlibs template
    output: list:
        string, filled madlibs template
        list: madlibs words to prompt to the user
    """
    if madlibs_template[0] is False:
        print(madlibs_template[1])
    else:
        print('Here is your madlib!')


def prompt_for_words(words):
    """
    This takes a list of words, prompts the user for them, then returns them
    formatted for python string formatting

    input: list, of madlibs template words
    output: list, of words the user entered
    """
    pass


def output_to_user():
    """
    This takes in the completed madlibs template, prints to the user, and asks
    if they would like to save. If so, they can put in a filename and it will
    write to a file.

    input: madlibs string
    output: none
    """
    pass


def exit():
    """
    this just prints a message and exits.

    No input or output
    """
    print('Thanks for playing!')
    sys.exit()


def run():
    """
    this is the brains of the operation

    This runs the whole madlibs program.
    """
    greet_user_prompt()
    while True:
        unformatted_madlibs = read_madlib_file()
        process_madlibs_template(unformatted_madlibs)



if __name__ == "__main__":
    run()
