# coding=utf-8
"""Dealloc Dealloc feature tests."""

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

@scenario('deallocDealloc.feature', 'Code with dealloc dealloc')
def test_code_with_dealloc_dealloc():
    pass


@scenario('deallocDealloc.feature', 'Code without dealloc dealloc')
def test_code_without_dealloc_dealloc():
    pass


@given('<filename>.c doesn\'t have dealloc dealloc')
def doesnt_have_dealloc_dealloc():
    global filename
    global expected

    filename = './support/good_deallocDealloc.txt'
    expected = ['good.c']

@given('<filename>.c has dealloc dealloc')
def has_dealloc_dealloc():
    global filename

    filename = './support/bad_deallocDealloc.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Ponteiro foi liberado duas vezes"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Ponteiro foi liberado duas vezes)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
