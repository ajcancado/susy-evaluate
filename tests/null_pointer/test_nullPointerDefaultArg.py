# coding=utf-8
"""Null Pointer Default Argument feature tests."""

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

@scenario('nullPointerDefaultArg.feature', 'Code with null pointer default argument')
def test_code_with_null_pointer_default_argument():
    pass


@scenario('nullPointerDefaultArg.feature', 'Code without null pointer default argument')
def test_code_without_null_pointer_default_argument():
    pass


@given('<filename>.c doesn\'t have null pointer default argument')
def doesnt_have_null_pointer_default_argument():
    global filename
    global expected

    filename = './support/good_nullPointerDefaultArg.txt'
    expected = ['good.c']


@given('<filename>.c has null pointer default argument')
def has_null_pointer_default_argument():
    global filename

    filename = './support/bad_nullPointerDefaultArg.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso a ponteiro nulo se o valor padrão foi utilizado"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Possível acesso a ponteiro nulo se o valor padrão foi utilizado)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Possível acesso a ponteiro nulo se o valor padrão foi utilizado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Possível acesso a ponteiro nulo se o valor padrão foi utilizado)', line)
            assert m == None