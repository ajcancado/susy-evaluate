# coding=utf-8
"""Invalid Print Argument Type String feature tests."""

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

@scenario('invalidPrintfArgType_s.feature', 'Code with invalid print argument type string')
def test_code_with_invalid_print_argument_type_string():
   pass


@scenario('invalidPrintfArgType_s.feature', 'Code without invalid print argument type string')
def test_code_without_invalid_print_argument_type_string():
    pass


@given('<filename>.c doesn\'t have invalid print argument type string')
def doesnt_have_invalid_print_argument_type_string():
    global filename
    global expected

    filename = './support/good_invalidPrintfArgType_s.txt'
    expected = ['good.c']


@given('<filename>.c has invalid print argument type string')
def has_invalid_print_argument_type_string():
    global filename

    filename = './support/bad_invalidPrintfArgType_s.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento do tipo \'string/char*\' no formato apresentado é inválido"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Argumento do tipo \'string/char*\' no formato apresentado é inválido)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Argumento do tipo \'string/char*\' no formato apresentado é inválido"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Argumento do tipo \'string/char*\' no formato apresentado é inválido)', line)
            assert m == None