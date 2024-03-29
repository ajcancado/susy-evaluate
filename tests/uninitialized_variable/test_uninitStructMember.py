# coding=utf-8
"""Uninitialized Struct Member feature tests."""

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

@scenario('uninitStructMember.feature', 'Code with uninitialized struct member')
def test_code_with_uninitialized_struct_member():
    pass


@scenario('uninitStructMember.feature', 'Code without uninitialized struct member')
def test_code_without_uninitialized_struct_member():
    pass


@given('<filename>.c doesn\'t have uninitialized struct member')
def doesnt_have_uninitialized_struct_member():
    global filename
    global expected

    filename = './support/good_uninitStructMember.txt'
    expected = ['good.c']

@given('<filename>.c has uninitialized struct member')
def has_uninitialized_struct_member():
    global filename

    filename = './support/bad_uninitStructMember.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma \'struct\' mas não foi inicializada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Variável foi criada em uma \'struct\' mas não foi inicializada)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Variável foi criada em uma \'struct\' mas não foi inicializada"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line

            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Variável foi criada em uma \'struct\' mas não foi inicializada)', line)
            assert m == None
