# coding=utf-8
"""possible Buffer Access Out Bounds feature tests."""

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

@scenario('possibleBufferAccessOutBounds.feature', 'Code with possible buffer access out bounds')
def test_code_with_possible_buffer_access_out_bounds():
    pass


@scenario('possibleBufferAccessOutBounds.feature', 'Code without possible buffer access out bounds')
def test_code_without_possible_buffer_access_out_bounds():
    pass


@given('<filename>.c doesn\'t have possible buffer access out bounds')
def doesnt_have_possible_buffer_access_out_bounds():
    global filename
    global expected

    filename = './support/good_possibleBufferAccessOutBounds.txt'
    expected = ['good.c']

@given('<filename>.c has possible buffer access out bounds')
def has_possible_buffer_access_out_bounds():
    global filename

    filename = './support/bad_possibleBufferAccessOutBounds.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso inválido"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Possível acesso inválido)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Possível acesso inválido"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Possível acesso inválido)', line)
            assert m == None