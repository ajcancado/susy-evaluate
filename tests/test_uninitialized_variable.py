# coding=utf-8
"""Uninitialized variables feature tests."""

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

@scenario('uninitialized_variable.feature', 'Code with uninitialized variables')
def test_code_with_uninitialized_variables():
    pass


@scenario('uninitialized_variable.feature', 'Code without uninitialized variables')
def test_code_without_uninitialized_variables():
    pass


@given('a2.c doesn\'t have uninitialized variables')
def the_code_doesnt_have_uninitialized_variables():
        global filename
        global expected

        filename = './support/case2_uninitialized_variable.txt'
        expected = ['a2.c']


@given('a1.c has uninitialized variables')
def the_code_has_uninitialized_variables():
        global filename

        filename = './support/case1_uninitialized_variable.txt'


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    subprocess.check_output('../main.py ' + filename, shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (error) Variável não inicializada"')
def i_should_receive_message_error():
        global filename

        with open("output.txt",'r') as f_out:

            for line in f_out:
                m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Variável não inicializada)', line)
                assert m != None


@then('shows me "[a2.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "a2.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None