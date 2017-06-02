# coding=utf-8
"""Redundant assignment feature tests."""

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

@scenario('redundant_assignment.feature', 'Code with redundant assignment')
def test_code_with_redundant_assignment():
    pass

@scenario('redundant_assignment.feature', 'Code without redundant assignment')
def test_code_without_redundant_assignment():
    pass

@given('a2.c doesn\'t have redundant assignment')
def doesnt_have_redundant_assignment():
    global filename
    global expected

    filename = './support/case2_redundant_assignment.txt'
    expected = ['a2.c']

@given('a1.c has redundant assignment')
def has_redundant_assignment():
    global filename

    filename = './support/case1_redundant_assignment.txt'
    
@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Atribuição redundante"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Atribuição redundante)', line)
            assert m != None

@then('shows me "[a2.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "a2.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
