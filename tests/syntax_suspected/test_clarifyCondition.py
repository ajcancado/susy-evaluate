# coding=utf-8
"""Clarify Condition feature tests."""

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

@scenario('clarifyCondition.feature', 'Code with clarify condition')
def test_code_with_clarify_condition():
    pass


@scenario('clarifyCondition.feature', 'Code without clarify condition')
def test_code_without_clarify_condition():
    pass


@given('<filename>.c doesn\'t have clarify condition')
def doesnt_have_clarify_condition():
    global filename
    global expected

    filename = './support/good_clarifyCondition.txt'
    expected = ['good.c']


@given('<filename>.c has clarify condition')
def has_clarify_condition():
    global filename

    filename = './support/bad_clarifyCondition.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Condição não esta claramente definida"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Condição não esta claramente definida)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None