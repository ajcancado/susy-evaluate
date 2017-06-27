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
            assert ("[" + f + "]: Nada para reportar") in contents


@scenario('input.feature', 'Files without errors reported by cppcheck')
def test_files_without_errors():
    pass


@given('case3_input.txt contains a file list without programming errors: a1.c')
def file_list_without_programming_errors_a1c():
    global filename
    global expected

    filename = './support/case3_input.txt'
    expected = ["a1.c"]


@then('shows me "[<filename>.c]: Nada para reportar"')
def shows_nothing():
    global expected

    with open("output.txt",'r') as f_out:
        for line in f_out:
            assert "a1.c" in line

            m = re.search('(\[[0-9A-Za-z\_]*\.\w\])\:\sNada para reportar', line)
            assert m != None


@scenario('input.feature', 'Files with invalid path')
def test_files_with_invalid_path():
    pass


@given('case4_input.txt contains a file list with invalid path')
def file_list_with_invalid_path():
    global filename
    global unexpected

    filename = './support/case4_input.txt'
    unexpected = ["a1.c"]


@then('files with invalid path will not analyzed')
def files_with_invalid_path_will_not_analyzed():
    global unexpected

    with open("output.txt",'r') as f_out:
        contents = f_out.read()

        for f in unexpected:
            assert f not in contents


@scenario('input.feature', 'Files with invalid extension')
def test_files_with_invalid_extension():
    pass


@given('case5_input.txt contains a file list with invalid extension')
def file_list_with_invalid_extension():
    global filename
    global expected

    filename = './support/case5_input.txt'
    expected = ""


@then('files with invalid extension will not analyzed')
def files_with_invalid_extension_will_not_analyzed():
    global expected

    with open("output.txt",'r') as f_out:
        m = re.search('(\[\w*\.((c|h|cpp|hpp){1})(\:\d+)?\])', f_out.read())
        assert m != None


@scenario('input.feature', 'Source and header files have programming errors')
def test_source_and_header_files_have_programming_errors():
    pass


@given('case6_input.txt contains a source and header files with programming errors')
def source_and_header_files_with_programming_errors():
    global filename
    global expected

    filename = './support/case6_input.txt'
    expected = 4 #numero de arquivos analisados


@then('shows me a file list with programming errors: source.c, header.h')
def shows_me_a_file_list_with_programming_errors_source_header():
    global expected

    with open("output.txt",'r') as f_out:
        assert len(f_out.readlines()) == expected
