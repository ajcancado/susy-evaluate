# coding=utf-8
"""Null pointer dereference feature tests."""

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

@scenario('null_pointer.feature', 'Code with null pointer dereference')
def test_code_with_null_pointer_dereference():
    pass


@scenario('null_pointer.feature', 'Code without null pointer dereference')
def test_code_without_null_pointer_dereference():
    pass


@given('<filename>.c doesn\'t have null pointer dereference')
def the_code_doesnt_have_null_pointer_dereference():
    global filename
    global expected

    filename = './support/good_null_pointer.txt'
    expected = ['good.c']


@given('<filename>.c has null pointer dereference')
def the_code_has_null_pointer_dereference():
    global filename

    filename = './support/bad_null_pointer.txt'


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (error) Desreferenciamento de ponteiro nulo"')
def i_should_receive_message_error():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Desreferenciamento de ponteiro nulo)', f_out.read())
        assert m != None


@then('it doesn\'t show me "[<filename>.c:<linha>]: (error) Desreferenciamento de ponteiro nulo"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Desreferenciamento de ponteiro nulo)', line)
            assert m == None
