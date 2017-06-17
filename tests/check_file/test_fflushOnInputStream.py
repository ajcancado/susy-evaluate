# coding=utf-8
"""fflush On Input Stream feature tests."""

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

@scenario('fflushOnInputStream.feature', 'Code with fflush on input stream')
def test_code_with_fflush_on_input_stream():
    pass

@scenario('fflushOnInputStream.feature', 'Code without fflush on input stream')
def test_code_without_fflush_on_input_stream():
    pass

@given('<filename>.c doesn\'t have fflush on input stream')
def doesnt_have_fflush_on_input_stream():
    global filename
    global expected

    filename = './support/good_fflushOnInputStream.txt'
    expected = ['good.c']

@given('<filename>.c has fflush on input stream')
def has_fflush_on_input_stream():
    global filename

    filename = './support/bad_fflushOnInputStream.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Chamada de função fflush() no stream de entrada, podendo resultar em comportamento indefinido em sistemas não-linux"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Chamada de função fflush() no stream de entrada, podendo resultar em comportamento indefinido em sistemas não-linux)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
