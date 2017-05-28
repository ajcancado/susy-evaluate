# coding=utf-8
"""Memory leak feature tests."""

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

@scenario('memory_leak.feature', 'Code with memory leak')
def test_code_with_memory_leak():
    pass

@scenario('memory_leak.feature', 'Code without memory leak')
def test_code_without_memory_leak():
    pass

@given('the code doesn\'t have memory leak')
def doesnt_have_memory_leak():
    global filename
    global expected

    filename = './support/case2_memory_leak.txt'
    expected = ""

@given('the code has memory leak')
def has_memory_leak():
    global filename

    filename = './support/case1_memory_leak.txt'
    
@when('it is submitted to the app')
def submitted():
   subprocess.check_output('../main.py ' + filename, shell=True)

@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de memória"')
def receive_message():
    global filename

    with open("output.txt",'r') as f_out:

        for line in f_out:
            m = re.search('[\[\]\:\w\.\_]*\s(\(erro\) Vazamento de memória)', line)
            assert m != None

@then('I shouldn\'t receive any messages')
def receive_no_messages():
    with open("output.txt",'r') as f_out:
        contents = f_out.read().strip()
        assert len(contents) == 0