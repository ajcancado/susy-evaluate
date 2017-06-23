# coding=utf-8
"""Uninitialized data feature tests."""

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

@scenario('uninitdata.feature', 'Code with uninitialized data')
def test_code_with_uninitialized_data():
    pass


@scenario('uninitdata.feature', 'Code without uninitialized data')
def test_code_without_uninitialized_data():
    pass


@given('<filename>.c doesn\'t have uninitialized data')
def doesnt_have_uninitialized_data():
    global filename
    global expected

    filename = './support/good_uninitdata.txt'
    expected = ['good.c']

@given('<filename>.c has uninitialized data')
def has_uninitialized_data():
    global filename

    filename = './support/bad_uninitdata.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Memória foi alocada mas não foi inicializada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Memória foi alocada mas não foi inicializada)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Memória foi alocada mas não foi inicializada"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line

            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Memória foi alocada mas não foi inicializada)', line)
            assert m == None
