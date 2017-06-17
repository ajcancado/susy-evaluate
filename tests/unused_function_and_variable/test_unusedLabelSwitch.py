# coding=utf-8
"""Unused Label Switch feature tests."""

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

@scenario('unusedLabelSwitch.feature', 'Code with unused label switch')
def test_code_with_unused_label_switch():
    pass


@scenario('unusedLabelSwitch.feature', 'Code without unused label switch')
def test_code_without_unused_label_switch():
    pass


@given('<filename>.c doesn\'t have unused label switch')
def doesnt_have_unused_label_switch():
    global filename
    global expected

    filename = './support/good_unusedLabelSwitch.txt'
    expected = ['good.c']


@given('<filename>.c has unused label switch')
def has_unused_label_switch():
    global filename

    filename = './support/bad_unusedLabelSwitch.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Label não utilizado"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Label não utilizado)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
