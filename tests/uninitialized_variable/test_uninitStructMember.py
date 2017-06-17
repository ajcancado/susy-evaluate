# coding=utf-8
"""Uninitiazed Struct Member feature tests."""

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

@scenario('uninitStructMember.feature', 'Code with uninitiazed struct member')
def test_code_with_uninitiazed_struct_member():
    pass


@scenario('uninitStructMember.feature', 'Code without uninitiazed struct member')
def test_code_without_uninitiazed_struct_member():
    pass


@given('<filename>.c doesn\'t have uninitiazed struct member')
def doesnt_have_uninitiazed_struct_member():
    global filename
    global expected

    filename = './support/good_uninitStructMember.txt'
    expected = ['good.c']

@given('<filename>.c has uninitiazed struct member')
def has_uninitiazed_struct_member():
    global filename

    filename = './support/bad_uninitStructMember.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma \'struct\' mas não foi inicializada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Variável foi criada em uma \'struct\' mas não foi inicializada)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
