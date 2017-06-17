# coding=utf-8
"""Read Write Only File feature tests."""

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

@scenario('readWriteOnlyFile.feature', 'Code with read write only file')
def test_code_with_read_write_only_file():
    pass


@scenario('readWriteOnlyFile.feature', 'Code without read write only file')
def test_code_without_read_write_only_file():
    pass


@given('<filename>.c doesn\'t have read write only file')
def doesnt_have_read_write_only_file():
    global filename
    global expected

    filename = './support/good_readWriteOnlyFile.txt'
    expected = ['good.c']

@given('<filename>.c has read write only file')
def has_read_write_only_file():
    global filename

    filename = './support/bad_readWriteOnlyFile.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de leitura em um arquivo que foi aberto somente para escrita"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Operação de leitura em um arquivo que foi aberto somente para escrita)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
