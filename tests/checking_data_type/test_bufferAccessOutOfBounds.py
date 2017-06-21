# coding=utf-8
"""Buffer Access Out Of Bounds feature tests."""

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

@scenario('bufferAccessOutOfBounds.feature', 'Code with buffer access out Of bounds')
def test_code_with_buffer_access_out_of_bounds():
    pass


@scenario('bufferAccessOutOfBounds.feature', 'Code without buffer access out Of bounds')
def test_code_without_buffer_access_out_of_bounds():
    pass


@given('<filename>.c doesn\'t have buffer access out Of bounds')
def doesnt_have_buffer_access_out_of_bounds():
    global filename
    global expected

    filename = './support/good_bufferAccessOutOfBounds.txt'
    expected = ['good.c']


@given('<filename>.c has buffer access out Of bounds')
def has_buffer_access_out_of_bounds():
    global filename

    filename = './support/bad_bufferAccessOutOfBounds.txt'

@when('it is submitted to the app')
def submitted():
    global filename
    subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Vetor acessado em índice inválido, portanto fora do seu limite"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Vetor acessado em índice inválido, portanto fora do seu limite)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None