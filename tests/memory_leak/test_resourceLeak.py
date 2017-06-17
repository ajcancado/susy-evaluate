# coding=utf-8
"""Resource Leak feature tests."""

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


@scenario('resourceLeak.feature', 'Code with resource leak')
def test_code_with_resource_leak():
    pass


@scenario('resourceLeak.feature', 'Code without resource leak')
def test_code_without_resource_leak():
    pass


@given('<filename>.c doesn\'t have resource leak')
def doesnt_have_resource_leak():
    global filename
    global expected

    filename = './support/good_resourceLeak.txt'
    expected = ['good.c']

@given('<filename>.c has resource leak')
def has_resource_leak():
    global filename

    filename = './support/bad_resourceLeak.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de recursos"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Vazamento de recursos)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
