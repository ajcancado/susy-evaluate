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

@given('case1_input.txt contains a list of files: a1.c and a2.c')
def file_with_list_of_files():
    global filename
    global expected

    filename = './support/case1_input.txt'
    expected = ["a1.c", "a2.c"]

@when('I call the app with the file as parameter')
def call_the_app():
   global result

   result = subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('shows me a list of files with errors: a1.c')
def shows_errors():

    global filename
    global expected
    global unexpected

    with open("output.txt",'r') as f_out:
        contents = f_out.read()

        for f in expected:
            assert f in contents

        for f in unexpected:
            assert ("[" + f + "]: Nenhum erro de análise estática foi encontrado") in contents

@scenario('input.feature', 'Not all files have errors reported by cppcheck')
def test_input_file_without_errors():
    pass


@given('case2_input.txt contains a list of good and bad files: a1.c and a2.c')
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

@given('case3_input.txt contains a list of good file: a1.c')
def file_with_list_of_good_files():
    global filename
    global expected

    filename = './support/case3_input.txt'
    expected = ["a1.c"]
    
@then('shows me "[a1.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "a1.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
