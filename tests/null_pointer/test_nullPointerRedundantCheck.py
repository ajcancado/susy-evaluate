# coding=utf-8
"""Null Pointer Redundant Check feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('null_pointer/nullPointerRedundantCheck.feature', 'Code with null pointer redundant check')
def test_code_with_null_pointer_redundant_check():
    """Code with null pointer redundant check."""


@scenario('null_pointer/nullPointerRedundantCheck.feature', 'Code without null pointer redundant check')
def test_code_without_null_pointer_redundant_check():
    """Code without null pointer redundant check."""


@given('<filename>.c doesn't have null pointer redundant check')
def filenamec_doesnt_have_null_pointer_redundant_check():
    """<filename>.c doesn't have null pointer redundant check."""


@given('<filename>.c has null pointer redundant check')
def filenamec_has_null_pointer_redundant_check():
    """<filename>.c has null pointer redundant check."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Existe uma possibilidade do valor acessado do ponteiro ser nulo"')
def i_should_receive_the_following_message_filenameclinha_erro_existe_uma_possibilidade_do_valor_acessado_do_ponteiro_ser_nulo():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Existe uma possibilidade do valor acessado do ponteiro ser nulo"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

