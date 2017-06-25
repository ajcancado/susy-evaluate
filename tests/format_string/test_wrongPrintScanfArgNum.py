# coding=utf-8
"""Wrong Print Scanf Argument Number feature tests."""

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


@scenario('wrongPrintScanfArgNum.feature', 'Code with wrong print scanf argument number')
def test_code_with_wrong_print_scanf_argument_number():
    pass


@scenario('wrongPrintScanfArgNum.feature', 'Code without wrong print scanf argument number')
def test_code_without_wrong_print_scanf_argument_number():
    pass


@given('<filename>.c doesn\'t have wrong print scanf argument number')
def doesnt_have_wrong_print_scanf_argument_number():
    global filename
    global expected

    filename = './support/good_wrongPrintScanfArgNum.txt'
    expected = ['good.c']

@given('<filename>.c has wrong print scanf argument number')
def has_wrong_print_scanf_argument_number():
    global filename

    filename = './support/bad_wrongPrintScanfArgNum.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Número de variáveis utilizadas não corresponde com o número de formatadores"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Número de variáveis utilizadas não corresponde com o número de formatadores)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Número de variáveis utilizadas não corresponde com o número de formatadores"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Número de variáveis utilizadas não corresponde com o número de formatadores)', line)
            assert m == None