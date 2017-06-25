# coding=utf-8
"""Truncated Long Cast Assignment feature tests."""

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

@scenario('truncLongCastAssignment.feature', 'Code with truncated long cast assignment')
def test_code_with_truncated_long_cast_assignment():
    pass


@scenario('truncLongCastAssignment.feature', 'Code without truncated long cast assignment')
def test_code_without_truncated_long_cast_assignment():
    pass


@given('<filename>.c doesn\'t have truncated long cast assignment')
def doesnt_have_truncated_long_cast_assignment():
    global filename
    global expected

    filename = './support/good_memory_leak.txt'
    expected = ['good.c']

@given('<filename>.c has truncated long cast assignment')
def has_truncated_long_cast_assignment():
    global filename

    filename = './support/bad_truncLongCastAssignment.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação)', line)
            assert m == None
