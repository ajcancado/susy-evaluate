# coding=utf-8
"""Truncated Long Cast Return feature tests."""

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

@scenario('truncLongCastReturn.feature', 'Code with truncated long cast return')
def test_code_with_truncated_long_cast_return():
    pass

@scenario('truncLongCastReturn.feature', 'Code without truncated long cast return')
def test_code_without_truncated_long_cast_return():
    pass


@given('<filename>.c doesn\'t have truncated long cast return')
def doesnt_have_truncated_long_cast_return():
    global filename
    global expected

    filename = './support/good_truncLongCastReturn.txt'
    expected = ['good.c']


@given('<filename>.c has truncated long cast return')
def has_truncated_long_cast_return():
    global filename

    filename = './support/bad_truncLongCastReturn.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é retornado como valor longo, podendo ocasionalmente haver perda de informação"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Resultado inteiro é retornado como valor longo, podendo ocasionalmente haver perda de informação)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None