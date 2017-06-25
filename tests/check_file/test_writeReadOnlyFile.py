# coding=utf-8
"""Write Read Only File feature tests."""

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


@scenario('writeReadOnlyFile.feature', 'Code with write read only file')
def test_code_with_write_read_only_file():
    pass


@scenario('writeReadOnlyFile.feature', 'Code without write read only file')
def test_code_without_write_read_only_file():
    pass


@given('<filename>.c doesn\'t have write read only file')
def doesnt_have_write_read_only_file():
    global filename
    global expected

    filename = './support/good_writeReadOnlyFile.txt'
    expected = ['good.c']

@given('<filename>.c has write read only file')
def has_write_read_only_file():
    global filename

    filename = './support/bad_writeReadOnlyFile.txt'


@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de escrita em um arquivo que foi aberto somente para leitura"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Operação de escrita em um arquivo que foi aberto somente para leitura)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Operação de escrita em um arquivo que foi aberto somente para leitura"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Operação de escrita em um arquivo que foi aberto somente para leitura)', line)
            assert m == None
