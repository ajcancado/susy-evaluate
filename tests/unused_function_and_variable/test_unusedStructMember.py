# coding=utf-8
"""Unused Struct Member feature tests."""

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

@scenario('unusedStructMember.feature', 'Code with unused struct member')
def test_code_with_unused_struct_member():
    pass


@scenario('unusedStructMember.feature', 'Code without unused struct member')
def test_code_without_unused_struct_member():
    pass


@given('<filename>.c doesn\'t have unused struct member')
def doesnt_have_unused_struct_member():
    global filename
    global expected

    filename = './support/good_unusedStrucMember.txt'
    expected = ['good.c']

@given('<filename>.c has unused struct member')
def has_unused_struct_member():
    global filename

    filename = './support/bad_unusedStrucMember.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma \'struct\' mas não foi utilizada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Variável foi criada em uma \'struct\' mas não foi utilizada)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
