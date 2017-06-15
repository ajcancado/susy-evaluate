# coding=utf-8
"""Null Pointer Arithmetic feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('null_pointer/nullPointerArithmetic.feature', 'Code with null pointer arithmetic')
def test_code_with_null_pointer_arithmetic():
    """Code with null pointer arithmetic."""


@scenario('null_pointer/nullPointerArithmetic.feature', 'Code without null pointer arithmetic')
def test_code_without_null_pointer_arithmetic():
    """Code without null pointer arithmetic."""


@given('<filename>.c doesn't have null pointer arithmetic')
def filenamec_doesnt_have_null_pointer_arithmetic():
    """<filename>.c doesn't have null pointer arithmetic."""


@given('<filename>.c has null pointer arithmetic')
def filenamec_has_null_pointer_arithmetic():
    """<filename>.c has null pointer arithmetic."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow na aritmética de ponteiro, ponteiro nulo é subtraído"')
def i_should_receive_the_following_message_filenameclinha_erro_overflow_na_aritmética_de_ponteiro_ponteiro_nulo_é_subtraído():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow na aritmética de ponteiro, ponteiro nulo é subtraído"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

