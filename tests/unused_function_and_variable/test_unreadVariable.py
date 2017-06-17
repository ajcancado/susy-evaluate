# coding=utf-8
"""Unread Variable feature tests."""

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

@scenario('unreadVariable.feature', 'Code with unread variable')
def test_code_with_unread_variable():
    pass


@scenario('unreadVariable.feature', 'Code without unread variable')
def test_code_without_unread_variable():
    pass


@given('<filename>.c doesn\'t have unread variable')
def doesnt_have_unread_variable():
    global filename
    global expected

    filename = './support/good_unreadVariable.txt'
    expected = ['good.c']

@given('<filename>.c has unread variable')
def has_unread_variable():
    global filename

    filename = './support/bad_unreadVariable.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Atribuição de valor à variável mas nunca utilizado"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Atribuição de valor à variável mas nunca utilizado)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
