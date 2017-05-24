# coding=utf-8
"""Input feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)

import subprocess 
import re

filename = ""
result = None

@scenario('input.feature', 'All files have errors reported by cppcheck')
def test_input_file():
    pass

@given('a file that contains a list of files')
def file_with_list_of_files():
    global filename

    filename = './suport/file.txt'

@when('I call the app with the file as parameter')
def call_the_app():
   global result

   result = subprocess.check_output('../main.py ' + filename, shell=True)


@then('shows me a list of files with errors')
def shows_errors():

    global filename

    with open("output.txt",'r') as f_out:
        contents = f_out.read()

        with open(filename, 'r') as f_in:
            for line in f_in:
                c = line.rstrip().split('/')[-1] #<name of file>.c
                assert c in contents

