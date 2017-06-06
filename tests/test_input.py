# coding=utf-8
"""Input feature tests."""

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
unexpected = []

@scenario('input.feature', 'All files have errors reported by cppcheck')
def test_all_files_have_errors():
    pass


@given('case1_input.txt contains a file list with programming errors: a1.c and a2.c')
def file_list_with_programming_errors_a1c_and_a2c():
    global filename
    global expected

    filename = './support/case1_input.txt'
    expected = ["a1.c", "a2.c"]


@when('I call the app with the container file as parameter')
def call_the_app():
    global result

    result = subprocess.check_output('../susy-avalia.py ' + filename + ' > output.txt', shell=True)

@then('shows me a file list with programming errors: a1.c, a2.c')
def shows_me_a_file_list_with_programming_errors_a1c_a2c():
    global expected

    with open("output.txt",'r') as f_out:
        contents = f_out.read()

        for f in expected:
            assert f in contents


@scenario('input.feature', 'Not all files have errors reported by cppcheck')
def test_not_all_files_have_errors():
    pass

@given('case2_input.txt contains a file with programming errors and a file without programming errors: a1.c and a2.c')
def file_with_programming_errors_and_a_file_without_programming_errors_a1c_and_a2c():
    global filename
    global expected
    global unexpected

    filename = './support/case2_input.txt'
    expected = ["a1.c"]
    unexpected = ["a2.c"]


@then('shows me a file list with programming errors: a1.c')
def shows_me_a_file_list_with_programming_errors_a1c():
    global filename
    global expected
    global unexpected

    with open("output.txt",'r') as f_out:
        contents = f_out.read()

        for f in expected:
            assert f in contents

        for f in unexpected:
            assert ("[" + f + "]: Nenhum erro de análise estática foi encontrado") in contents


@scenario('input.feature', 'Files without errors reported by cppcheck')
def test_files_without_errors():
    pass


@given('case3_input.txt contains a file list without programming errors: a1.c')
def file_list_without_programming_errors_a1c():
    global filename
    global expected

    filename = './support/case3_input.txt'
    expected = ["a1.c"]


@then('shows me "[a1.c]: Nenhum erro de análise estática foi encontrado"')
def shows_nothing():
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "a1.c" in line

            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNenhum erro de análise estática foi encontrado', line)
            assert m != None
