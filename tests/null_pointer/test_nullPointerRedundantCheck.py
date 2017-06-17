# coding=utf-8
"""Null Pointer Redundant Check feature tests."""

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


@scenario('nullPointerRedundantCheck.feature', 'Code with null pointer redundant check')
def test_code_with_null_pointer_redundant_check():
    pass


@scenario('nullPointerRedundantCheck.feature', 'Code without null pointer redundant check')
def test_code_without_null_pointer_redundant_check():
    pass

@given('<filename>.c doesn\'t have null pointer redundant check')
def doesnt_have_null_pointer_redundant_check():
    global filename
    global expected

    filename = './support/good_nullPointerRedudantCheck.txt'
    expected = ['good.c']

@given('<filename>.c has null pointer redundant check')
def has_null_pointer_redundant_check():
    global filename

    filename = './support/bad_nullPointerRedudantCheck.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Existe uma possibilidade do valor acessado do ponteiro ser nulo"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Existe uma possibilidade do valor acessado do ponteiro ser nulo)', line)
            assert m != None


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None