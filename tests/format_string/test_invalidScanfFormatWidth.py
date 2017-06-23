# coding=utf-8
"""Invalid Scanf Format Width feature tests."""

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

@scenario('invalidScanfFormatWidth.feature', 'Code with invalid scanf format width')
def test_code_with_invalid_scanf_format_width():
    pass


@scenario('invalidScanfFormatWidth.feature', 'Code without invalid scanf format width')
def test_code_without_invalid_scanf_format_width():
    pass


@given('<filename>.c doesn\'t have invalid scanf format width')
def doesnt_have_invalid_scanf_format_width():
    global filename
    global expected

    filename = './support/good_invalidScanfFormatWidth.txt'
    expected = ['good.c']

@given('<filename>.c has invalid scanf format width')
def has_invalid_scanf_format_width():
    global filename

    filename = './support/bad_invalidScanfFormatWidth.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Tamanho da variável no formato \'string/char*\' é inválida"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Tamanho da variável no formato \'string/char*\' é inválida)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Tamanho da variável no formato \'string/char*\' é inválida"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Tamanho da variável no formato \'string/char*\' é inválida)', line)
            assert m == None
