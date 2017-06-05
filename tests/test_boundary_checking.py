# coding=utf-8
"""Boundary checking feature tests."""

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

@scenario('boundary_checking.feature', 'Code with array accessed out of bounds')
def test_code_with_array_accessed_out_of_bounds():
    pass


@scenario('boundary_checking.feature', 'Code without array accessed out of bounds')
def test_code_without_array_accessed_out_of_bounds():
    pass


@given('a1.c has an array accessed out of bounds')
def the_code_has_an_array_accessed_out_of_bounds():
    global filename

    filename = './support/case1_boundary_checking.txt'


@given('a2.c doesn\'t have an array accessed out of bounds')
def the_code_doesnt_have_an_array_accessed_out_of_bounds():
    global filename
    global expected

    filename = './support/case2_boundary_checking.txt'
    expected = ['a2.c']


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (error) Array \'arr[3]\' acessado no índice 3, está fora dos limites"')
def i_should_receive_message_error():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Array \'arr[3]\' acessado no índice 3, está fora dos limites)', line)
            assert m != None


@then('shows me "[a2.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "a2.c" in line

            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
