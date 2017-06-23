# coding=utf-8
"""Dealloc Use feature tests."""

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


@scenario('deallocuse.feature', 'Code with dealloc use')
def test_code_with_dealloc_use():
    pass


@scenario('deallocuse.feature', 'Code without dealloc use')
def test_code_without_dealloc_use():
    pass


@given('<filename>.c doesn\'t have dealloc use')
def doesnt_have_dealloc_use():
    global filename
    global expected

    filename = './support/good_deallocuse.txt'
    expected = ['good.c']

@given('<filename>.c has dealloc use')
def has_memory_leak():
    global filename

    filename = './support/bad_deallocuse.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso a variável já desalocada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Acesso a variável já desalocada)', line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Acesso a variável já desalocada"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Acesso a variável já desalocada)', line)
            assert m == None