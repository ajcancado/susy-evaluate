# coding=utf-8
"""Double Free feature tests."""

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

@scenario('doubleFree.feature', 'Code with double free')
def test_code_with_double_free():
    pass


@scenario('doubleFree.feature', 'Code without double free')
def test_code_without_double_free():
    pass


@given('<filename>.c doesn\'t have double free')
def doesnt_have_double_free():
    global filename
    global expected

    filename = './support/good_doubleFree.txt'
    expected = ['good.c']


@given('<filename>.c has double free')
def has_double_free():
    global filename

    filename = './support/bad_doubleFree.txt'


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