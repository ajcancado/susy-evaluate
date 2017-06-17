# coding=utf-8
"""Float Conversion Overflow feature tests."""

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

@scenario('floatConversionOverflow.feature', 'Code with float conversion overflow')
def test_code_with_float_conversion_overflow():
    pass


@scenario('floatConversionOverflow.feature', 'Code without float conversion overflow')
def test_code_without_float_conversion_overflow():
    pass


@given('<filename>.c doesn\'t have float conversion overflow')
def doesnt_have_float_conversion_overflow():
    global filename
    global expected

    filename = './support/good_floatConversionOverflow.txt'
    expected = ['good.c']

@given('<filename>.c has float conversion overflow')
def has_float_conversion_overflow():
    global filename

    filename = './support/bad_floatConversionOverflow.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow de variável do tipo \'float\'"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Overflow de variável do tipo \'float\')', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
