# coding=utf-8
"""Unassigned Variable feature tests."""

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

@scenario('unassignedVariable.feature', 'Code with unassigned variable')
def test_code_with_unassigned_variable():
   pass


@scenario('unassignedVariable.feature', 'Code without unassigned variable')
def test_code_without_unassigned_variable():
    pass


@given('<filename>.c doesn\'t have unassigned variable')
def doesnt_have_unassigned_variable():
    global filename
    global expected

    filename = './support/good_unassignedVariable.txt'
    expected = ['good.c']

@given('<filename>.c has unassigned variable')
def has_unassigned_variable():
    global filename

    filename = './support/bad_unassignedVariable.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável não foi atribuída"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Variável não foi atribuída)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
