# coding=utf-8
"""Unused Variable feature tests."""

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


@scenario('unusedVariable.feature', 'Code with unused Variable')
def test_code_with_unused_variable():
    pass


@scenario('unusedVariable.feature', 'Code without unused Variable')
def test_code_without_unused_variable():
    pass


@given('<filename>.c doesn\'t have unused Variable')
def doesnt_have_unused_variable():
    global filename
    global expected

    filename = './support/good_unusedVariable.txt'
    expected = ['good.c']


@given('<filename>.c has unused Variable')
def has_unused_variable():
    global filename

    filename = './support/bad_unusedVariable.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável nunca foi utilizada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Variável nunca foi utilizada)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None


