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


@given('the code doesn\'t have null pointer dereference')
def the_code_doesnt_have_null_pointer_dereference():
    global filename
    global expected

    filename = './support/case2_null_pointer.txt'
    expected = ""


@given('the code has null pointer dereference')
def the_code_has_null_pointer_dereference():
    global filename

    filename = './support/case1_null_pointer.txt'


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    subprocess.check_output('../main.py ' + filename, shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (error) Desreferenciamento de ponteiro nulo"')
def i_should_receive_message_error():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Desreferencia a ponteiro nulo)', line)
            assert m != None


@then('I shouldn\'t receive any messages')
def i_shouldnt_receive_any_messages():
    with open("output.txt",'r') as f_out:
        contents = f_out.read().strip()
        assert len(contents) == 0
