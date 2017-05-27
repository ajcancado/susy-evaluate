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
expected = []
unexpected = []

@scenario('input.feature', 'All files have errors reported by cppcheck')
def test_input_file_with_errors():
    pass

@given('a file that contains a list of files')
def file_with_list_of_files():
    global filename
    global expected

    filename = './support/case1_input.txt'
    expected = ["a1.c", "a2.c"]

@when('I call the app with the file as parameter')
def call_the_app():
   global result

   result = subprocess.check_output('../main.py ' + filename, shell=True)


@then('shows me a list of files with errors')
def shows_errors():

    global filename
    global expected
    global unexpected

    with open("output.txt",'r') as f_out:
        contents = f_out.read()

        for f in expected:
            assert f in contents

        for f in unexpected:
            assert not (f in contents)

@scenario('input.feature', 'Not all files have errors reported by cppcheck')
def test_input_file_without_errors():
    pass


@given('a file that contains a list of good and bad files')
def file_with_list_of_good_and_bad_files():
    global filename
    global expected
    global unexpected

    filename = './support/case2_input.txt'
    expected = ["a1.c"]
    unexpected = ["a2.c"]

@scenario('input.feature', 'No files have errors reported by cppcheck')
def test_no_errors():
    pass
    
@then('shows me nothing')
def shows_anything():

    with open("output.txt",'r') as f_out:
        contents = f_out.read().strip()

        assert len(contents) == 0