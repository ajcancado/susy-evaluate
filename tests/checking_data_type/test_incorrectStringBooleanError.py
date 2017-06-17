# coding=utf-8
"""Incorrect String Boolean Error feature tests."""

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

@scenario('incorrectStringBooleanError.feature', 'Code with incorrect string boolean error')
def test_code_with_incorrect_string_boolean_error():
    pass


@scenario('incorrectStringBooleanError.feature', 'Code without incorrect string boolean error')
def test_code_without_incorrect_string_boolean_error():
    pass


@given('<filename>.c doesn\'t have incorrect string boolean error')
def doesnt_have_incorrect_string_boolean_error():
    global filename
    global expected

    filename = './support/good_incorrectStringBooleanError.txt'
    expected = ['good.c']

@given('<filename>.c has incorrect string boolean error')
def has_incorrect_string_boolean_error():
    global filename

    filename = './support/bad_incorrectStringBooleanError.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Conversão literal de variável tipo carácter para booleano sempre é verdadeiro"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Conversão literal de variável tipo carácter para booleano sempre é verdadeiro)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None