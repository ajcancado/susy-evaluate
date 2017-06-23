# coding=utf-8
"""Unused Function feature tests."""

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

@scenario('unusedFunction.feature', 'Code with unused function')
def test_code_with_unused_function():
    pass


@scenario('unusedFunction.feature', 'Code without unused function')
def test_code_without_unused_function():
    pass


@given('<filename>.c doesn\'t have unused function')
def doesnt_have_unused_function():
    global filename
    global expected

    filename = './support/good_unusedFunction.txt'
    expected = ['good.c']


@given('<filename>.c has unused function')
def has_unused_function():
    global filename

    filename = './support/bad_unusedFunction.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Função criada mas nunca foi utilizada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Função criada mas nunca foi utilizada)', line)
            assert m != None
            
@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Função criada mas nunca foi utilizada"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Função criada mas nunca foi utilizada)', line)
            assert m == None
