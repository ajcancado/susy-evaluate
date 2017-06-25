# coding=utf-8
"""Mismatch Allocation and Deallocation feature tests."""

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

@scenario('mismatchAllocDealloc.feature', 'Code with mismatch allocation and deallocation')
def test_code_with_mismatch_allocation_and_deallocation():
    pass


@scenario('mismatchAllocDealloc.feature', 'Code without mismatch allocation and deallocation')
def test_code_without_mismatch_allocation_and_deallocation():
   pass

@given('<filename>.c doesn\'t have mismatch allocation and deallocation')
def filenamec_doesnt_have_mismatch_allocation_and_deallocation():
    global filename
    global expected

    filename = './support/good_mismatchAllocDealloc.txt'
    expected = ['good.c']

@given('<filename>.c has mismatch allocation and deallocation')
def has_mismatch_allocation_and_deallocation():
    global filename

    filename = './support/bad_mismatchAllocDealloc.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Falta de alocação ou desalocação de memória"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Falta de alocação ou desalocação de memória)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Falta de alocação ou desalocação de memória"')
def shows_nothing():

    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Falta de alocação ou desalocação de memória)', line)
            assert m == None
