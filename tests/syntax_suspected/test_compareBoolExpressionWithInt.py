# coding=utf-8
"""Compare Bool Expression with Integer feature tests."""

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

@scenario('compareBoolExpressionWithInt.feature', 'Code with compare boolen expression with integer')
def test_code_with_compare_boolen_expression_with_integer():
    pass


@scenario('compareBoolExpressionWithInt.feature', 'Code without compare boolen expression with integer')
def test_code_without_compare_boolen_expression_with_integer():
    pass


@given('<filename>.c doesn\'t have compare boolen expression with integer')
def filenamec_doesnt_have_compare_boolen_expression_with_integer():
    global filename
    global expected

    filename = './support/good_compareBoolExpressionWithInt.txt'
    expected = ['good.c']

@given('<filename>.c has compare boolen expression with integer')
def filenamec_has_compare_boolen_expression_with_integer():
    global filename

    filename = './support/bad_compareBoolExpressionWithInt.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Comparação de tipo booleano com tipo inteiro"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Comparação de tipo booleano com tipo inteiro)', line)
            assert m != None

@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None