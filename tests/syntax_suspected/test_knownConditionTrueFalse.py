# coding=utf-8
"""Known condition true false feature tests."""

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

@scenario('knownConditionTrueFalse.feature', 'Code with known condition true false')
def test_code_with_known_condition_true_false():
    pass

@scenario('knownConditionTrueFalse.feature', 'Code without known condition true false')
def test_code_without_known_condition_true_false():
    pass

@given('<filename>.c doesn\'t have known condition true false')
def doesnt_have_known_condition_true_false():
    global filename
    global expected

    filename = './support/good_known_condition_true_false.txt'
    expected = ['good.c']

@given('<filename>.c has known condition true false')
def has_known_condition_true_false():
    global filename

    filename = './support/bad_known_condition_true_false.txt'
    
@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Condição sempre verdadeira ou falsa"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Condição sempre verdadeira ou falsa)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Condição sempre verdadeira ou falsa"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Condição sempre verdadeira ou falsa)', line)
            assert m == None
