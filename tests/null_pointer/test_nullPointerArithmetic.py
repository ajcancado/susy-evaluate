# coding=utf-8
"""Null Pointer Arithmetic feature tests."""

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

@scenario('nullPointerArithmetic.feature', 'Code with null pointer arithmetic')
def test_code_with_null_pointer_arithmetic():
    pass

@scenario('nullPointerArithmetic.feature', 'Code without null pointer arithmetic')
def test_code_without_null_pointer_arithmetic():
    pass

@given('<filename>.c doesn\'t have null pointer arithmetic')
def doesnt_have_null_pointer_arithmetic():
    global filename
    global expected

    filename = './support/good_nullPointerArithmetic.txt'
    expected = ['good.c']

@given('<filename>.c has null pointer arithmetic')
def has_null_pointer_arithmetic():    
    global filename

    filename = './support/bad_nullPointerArithmetic.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow na aritmética de ponteiro, ponteiro nulo é subtraído"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Overflow na aritmética de ponteiro, ponteiro nulo é subtraído)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
