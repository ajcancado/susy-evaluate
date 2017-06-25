# coding=utf-8
"""Unused Allocated Memory feature tests."""

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

@scenario('unusedAllocatedMemory.feature', 'Code with unused allocated memory')
def test_code_with_unused_allocated_memory():
    pass


@scenario('unusedAllocatedMemory.feature', 'Code without unused allocated memory')
def test_code_without_unused_allocated_memory():
    pass


@given('<filename>.c doesn\'t have unused allocated memory')
def filenamec_doesnt_have_unused_allocated_memory():
    global filename
    global expected

    filename = './support/good_unusedAllocatedMemory.txt'
    expected = ['good.c']

@given('<filename>.c has unused allocated memory')
def has_memory_leak():
    global filename

    filename = './support/bad_unusedAllocatedMemory.txt'

@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Recursos de memória alocados nunca foram utilizados"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:
        m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Recursos de memória alocados nunca foram utilizados)', f_out.read())
        assert m != None

@then('it doesn\'t show me "[<filename>.c:<linha>]: (erro) Recursos de memória alocados nunca foram utilizados"')
def shows_nothing( ):
    
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "good.c" in line
            
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Recursos de memória alocados nunca foram utilizados)', line)
            assert m == None
