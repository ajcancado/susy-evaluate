# coding=utf-8
"""Division by zero feature tests."""

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

@scenario('division_zero.feature', 'Code with division by zero')
def test_code_with_division_by_zero():
    pass


@scenario('division_zero.feature', 'Code without division by zero')
def test_code_without_division_by_zero():
    pass


@given('a1.c has a division by zero')
def the_code_has_a_division_by_zero():
    global filename

    filename = './support/case1_division_zero.txt'


@given('a2.c doesn\'t have a division by zero')
def the_code_doesnt_have_a_division_by_zero():
    global filename
    global expected

    filename = './support/case2_division_zero.txt'
    expected = ['a2.c']


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (error) Divisão por zero"')
def i_should_receive_message_error():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Divisão por zero)', line)
            assert m != None


@then('shows me "[a2.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "a2.c" in line

            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
