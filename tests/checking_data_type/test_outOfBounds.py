# coding=utf-8
"""Out Of Bounds feature tests."""

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

@scenario('outOfBounds.feature', 'Code with out of bounds')
def test_code_with_out_of_bounds():
    pass


@scenario('outOfBounds.feature', 'Code without out of bounds')
def test_code_without_out_of_bounds():
    pass


@given('<filename>.c doesn\'t have out of bounds')
def doesnt_have_out_of_bounds():
    global filename
    global expected

    filename = './support/good_outOfBounds.txt'
    expected = ['good.c']


@given('<filename>.c has out of bounds')
def has_out_of_bounds():
    global filename

    filename = './support/bad_outOfBounds.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso inválido"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Acesso inválido)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Acesso inválido"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Acesso inválido)', line)
            assert m == None