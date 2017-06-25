# coding=utf-8
"""Pointer Arith Boolean feature tests."""

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

@scenario('pointerArithBool.feature', 'Code with Pointer Arith Boolean')
def test_code_with_pointer_arith_boolean():
    pass


@scenario('pointerArithBool.feature', 'Code without Pointer Arith Boolean')
def test_code_without_pointer_arith_boolean():
    pass


@given('<filename>.c doesn\'t have Pointer Arith Boolean')
def doesnt_have_pointer_arith_boolean():
    global filename
    global expected

    filename = './support/good_pointerArithBool.txt'
    expected = ['good.c']


@given('<filename>.c has Pointer Arith Boolean')
def has_pointer_arith_boolean():
    global filename

    filename = './support/bad_pointerArithBool.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Valor booleano atribuído a ponteiro"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Valor booleano atribuído a ponteiro)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Valor booleano atribuído a ponteiro"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Valor booleano atribuído a ponteiro)', line)
            assert m == None