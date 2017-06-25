# coding=utf-8
"""Pointer Out Of Bounds feature tests."""

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

@scenario('pointerOutOfBounds.feature', 'Code with pointer out of bounds')
def test_code_with_pointer_out_of_bounds():
    pass


@scenario('pointerOutOfBounds.feature', 'Code without pointer out of bounds')
def test_code_without_pointer_out_of_bounds():
    pass


@given('<filename>.c doesn\'t have pointer out of bounds')
def doesnt_have_pointer_out_of_bounds():
    global filename
    global expected

    filename = './support/good_pointerOutOfBounds.txt'
    expected = ['good.c']

@given('<filename>.c has pointer out of bounds')
def has_pointer_out_of_bounds():
    global filename

    filename = './support/bad_pointerOutOfBounds.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso à posição inválida do ponteiro"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Acesso à posição inválida do ponteiro)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Acesso à posição inválida do ponteiro"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Acesso à posição inválida do ponteiro)', line)
            assert m == None