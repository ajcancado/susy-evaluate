# coding=utf-8
"""Invalid Scanf Argument Type Integer feature tests."""

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

@scenario('invalidScanfArgType_int.feature', 'Code with invalid scanf argument type integer')
def test_code_with_invalid_scanf_argument_type_integer():
    pass


@scenario('invalidScanfArgType_int.feature', 'Code without invalid scanf argument type integer')
def test_code_without_invalid_scanf_argument_type_integer():
    pass


@given('<filename>.c doesn\'t have invalid scanf argument type integer')
def doesnt_have_invalid_scanf_argument_type_integer():
    global filename
    global expected

    filename = './support/good_invalidScanfArgType_int.txt'
    expected = ['good.c']

@given('<filename>.c has invalid scanf argument type integer')
def has_invalid_scanf_argument_type_integer():
    global filename

    filename = './support/bad_invalidScanfArgType_int.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Scanf com argumento do tipo \'int\' inválido"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Scanf com argumento do tipo \'int\' inválido)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Scanf com argumento do tipo \'int\' inválido"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Scanf com argumento do tipo \'int\' inválido)', line)
            assert m == None
