# coding=utf-8
"""Memleak On Realloc feature tests."""

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

@scenario('memleakOnRealloc.feature', 'Code with memleak on realloc')
def test_code_with_memleak_on_realloc():
   pass


@scenario('memleakOnRealloc.feature', 'Code without memleak on realloc')
def test_code_without_memleak_on_realloc():
    pass


@given('<filename>.c doesn\'t have memleak on realloc')
def doesnt_have_memleak_on_realloc():
    global filename
    global expected

    filename = './support/good_memleakOnRealloc.txt'
    expected = ['good.c']


@given('<filename>.c has memleak on realloc')
def has_memleak_on_realloc():
    global filename

    filename = './support/bad_memleakOnRealloc.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de memória no processo de realocação"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Vazamento de memória no processo de realocação)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None