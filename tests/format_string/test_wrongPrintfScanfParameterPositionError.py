# coding=utf-8
"""Wrong Printf Scanf Parameter Position Error feature tests."""

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


@scenario('wrongPrintfScanfParameterPositionError.feature', 'Code with wrong printf scanf parameter position error')
def test_code_with_wrong_printf_scanf_parameter_position_error():
    pass


@scenario('wrongPrintfScanfParameterPositionError.feature', 'Code without wrong printf scanf parameter position error')
def test_code_without_wrong_printf_scanf_parameter_position_error():
    pass


@given('<filename>.c doesn\'t have wrong printf scanf parameter position error')
def doesnt_have_wrong_printf_scanf_parameter_position_error():
    global filename
    global expected

    filename = './support/good_wrongPrintfScanfParameterPositionError.txt'
    expected = ['good.c']

@given('<filename>.c has wrong printf scanf parameter position error')
def has_wrong_printf_scanf_parameter_position_error():
    global filename

    filename = './support/bad_wrongPrintfScanfParameterPositionError.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Referenciamento de parâmetro foi realizado incorretamente"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Referenciamento de parâmetro foi realizado incorretamente)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
