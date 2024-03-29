# coding=utf-8
"""Unprecise Math Call feature tests."""

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

@scenario('unpreciseMathCall.feature', 'Code with unprecise math call')
def test_code_with_unprecise_math_call():
    pass


@scenario('unpreciseMathCall.feature', 'Code without unprecise math call')
def test_code_without_unprecise_math_call():
    pass


@given('<filename>.c doesn\'t have unprecise math call')
def doesnt_have_unprecise_math_call():
    global filename
    global expected

    filename = './support/good_unpreciseMathCall.txt'
    expected = ['good.c']

@given('<filename>.c has unprecise math call')
def has_unprecise_math_call():
    global filename

    filename = './support/bad_unpreciseMathCall.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Passando valor que pode gerar resultado indefinido"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Passando valor que pode gerar resultado indefinido)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Passando valor que pode gerar resultado indefinido"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Passando valor que pode gerar resultado indefinido)', line)
            assert m == None