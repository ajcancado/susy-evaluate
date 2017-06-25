# coding=utf-8
"""Dealloc Return error feature tests."""

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

@scenario('deallocret.feature', 'Code with dealloc return error')
def test_code_with_dealloc_return_error():
    pass


@scenario('deallocret.feature', 'Code without dealloc return error')
def test_code_without_dealloc_return_error():
    pass


@given('<filename>.c doesn\'t have dealloc return error')
def doesnt_have_dealloc_return_error():
    global filename
    global expected

    filename = './support/good_deallocret.txt'
    expected = ['good.c']

@given('<filename>.c has dealloc return error')
def has_dealloc_return_error():
    global filename

    filename = './support/bad_deallocret.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Retorno/acesso de variável já desalocada"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Retorno/acesso de variável já desalocada)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Retorno/acesso de variável já desalocada"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Retorno/acesso de variável já desalocada)', line)
            assert m == None
