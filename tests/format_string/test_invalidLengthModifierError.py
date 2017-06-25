# coding=utf-8
"""Invalid Length Modifier Error feature tests."""

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

@scenario('invalidLengthModifierError.feature', 'Code with invalid length modifier error')
def test_code_with_invalid_length_modifier_error():
    pass


@scenario('invalidLengthModifierError.feature', 'Code without invalid length modifier error')
def test_code_without_invalid_length_modifier_error():
    pass


@given('<filename>.c doesn\'t have invalid length modifier error')
def doesnt_have_invalid_length_modifier_error():
    global filename
    global expected

    filename = './support/good_invalidLengthModifierError.txt'
    expected = ['good.c']

@given('<filename>.c has invalid length modifier error')
def has_invalid_length_modifier_error():
    global filename

    filename = './support/bad_invalidLengthModifierError.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Formato de \'string/char*\' modificado não pode ser utilizado sem conversão específica"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Formato de \'string/char*\' modificado não pode ser utilizado sem conversão específica)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Formato de \'string/char*\' modificado não pode ser utilizado sem conversão específica"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Formato de \'string/char*\' modificado não pode ser utilizado sem conversão específica)', line)
            assert m == None