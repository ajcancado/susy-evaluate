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

    filename = './support/good_unusedStructMember.txt'
    expected = ['good.c']

@given('<filename>.c has unused struct member')
def has_unused_struct_member():
    global filename

    filename = './support/bad_unusedStructMember.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma \'struct\' mas não foi utilizada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search("[\[\]\:\w\.\_]*\s(\(erro\) Variável foi criada em uma 'struct' mas não foi utilizada)", line)
            assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Variável foi criada em uma \'struct\' mas não foi utilizada"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search("[\[\]\:\w\.\_]*\s(\(erro\) Variável foi criada em uma 'struct' mas não foi utilizada)", line)
            assert m == None
