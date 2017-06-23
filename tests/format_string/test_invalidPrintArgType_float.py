# coding=utf-8
"""Invalid Print Argument Type Float feature tests."""

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

@scenario('invalidPrintArgType_float.feature', 'Code with invalid print argument type float')
def test_code_with_invalid_print_argument_type_float():
    pass


@scenario('invalidPrintArgType_float.feature', 'Code without invalid print argument type float')
def test_code_without_invalid_print_argument_type_float():
    pass


@given('<filename>.c doesn\'t have invalid print argument type float')
def doesnt_have_invalid_print_argument_type_float():
    global filename
    global expected

    filename = './support/good_invalidPrintArgType_float.txt'
    expected = ['good.c']

@given('<filename>.c has invalid print argument type float')
def has_invalid_print_argument_type_float():
    global filename

    filename = './support/bad_invalidPrintArgType_float.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento de tipo \'float\' é inválido neste caso"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Argumento de tipo \'float\' é inválido neste caso)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Argumento de tipo \'float\' é inválido neste caso"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Argumento de tipo \'float\' é inválido neste caso)', line)
            assert m == None
