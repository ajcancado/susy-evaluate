# coding=utf-8
"""Use Closed File feature tests."""

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


@scenario('useClosedFile.feature', 'Code with use closed file')
def test_code_with_use_closed_file():
    pass


@scenario('useClosedFile.feature', 'Code without use closed file')
def test_code_without_use_closed_file():
    pass


@given('<filename>.c doesn\'t have use closed file')
def doesnt_have_use_closed_file():
    global filename
    global expected

    filename = './support/good_useClosedFile.txt'
    expected = ['good.c']


@given('<filename>.c has use closed file')
def has_use_closed_file():
    global filename

    filename = './support/bad_useClosedFile.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Arquivo utilizado que não foi aberto"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Arquivo utilizado que não foi aberto)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Arquivo utilizado que não foi aberto"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Arquivo utilizado que não foi aberto)', line)
            assert m == None
