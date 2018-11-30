"""Madlibs! Open in the command line to play"""

from .file_io import read_file, write_file
from textwrap import dedent
import re
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


def prompt_user_filename():
    """
    Prompts the user for a filename

    no input, output: string
    """

    filename = ''
    while filename is '':
        filename = input('Your madlibs file (no extension): ')
        if filename is '':
            print('You must enter a filename!')

    return filename


def read_madlib_file(filename):
    """
    This takes the user's input, asks file_io to read the file,
    returns a list with the success/fail status of read, and content (or error
    message)

    No input
    output: list, bool fail/pass + madlibs template/error message
    """

    if filename.lower() == 'quit':
        exit()

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
    This takes in a madlibs template as a string, uses regex to gather all of
    the template words into a list and strip the {}, and also replace all the
    template words with {} so they can be filled with string format

    input: list:
        bool, fail/pass of read
        string, madlibs template
    output: list:
        bool, fail/pass
        string, filled madlibs template
    """

    if madlibs_template[0] is False:
        print(madlibs_template[1])
        return madlibs_template
    else:
        words = re.findall(r'\{.*?\}', madlibs_template[1])
        madlibs_template[1] = re.sub(r'\{.*?\}', '{}', madlibs_template[1])

        for i in range(len(words)):
            words[i] = words[i].strip('{}')

        user_words = prompt_for_words(words)

        madlibs_template[1] = madlibs_template[1].format(*user_words)

        return madlibs_template


def prompt_for_words(words):
    """
    This takes a list of words, prompts the user for them, then returns a list
    of user input

    input: list, of madlibs template words
    output: list, of words the user entered
    """

    print('Get ready to enter your words!')
    words_out = []

    for i in range(len(words)):
        user_input = input(words[i] + ': ')
        if user_input == 'quit':
            exit()

        words_out.append(user_input)

    return words_out


def output_to_user(madlibs_output):
    """
    This takes in the completed madlibs template, prints to the user, and asks
    if they would like to save. If so, they can put in a filename and it will
    write to a file.

    input: madlibs string
    output: none
    """
    if madlibs_output[0] is True:
        print('Your completed madlib:\n\n')
        print(madlibs_output[1])
        user_input = input('Enter y to save: ').lower()

        if user_input == 'quit':
            exit()
        if user_input == 'y':
            user_filename = input('please enter a filename: ')
            print(write_file(madlibs_output[1], user_filename))

    else:
        print('There was an error! Try again later!')


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
        unformatted_madlibs = read_madlib_file(prompt_user_filename())
        filled_madlibs = process_madlibs_template(unformatted_madlibs)
        if filled_madlibs[0] is True:
            output_to_user(filled_madlibs)

            user_input = input('Would you like to do another? y/n ')
            if user_input.lower() == 'y':
                continue
        else:
            continue

        exit()


if __name__ == "__main__":
    run()
