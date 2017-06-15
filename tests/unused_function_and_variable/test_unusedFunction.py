# coding=utf-8
"""Unused Function feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('unused_function_and_variable/unusedFunction.feature', 'Code with unused function')
def test_code_with_unused_function():
    """Code with unused function."""


@scenario('unused_function_and_variable/unusedFunction.feature', 'Code without unused function')
def test_code_without_unused_function():
    """Code without unused function."""


@given('<filename>.c doesn't have unused function')
def filenamec_doesnt_have_unused_function():
    """<filename>.c doesn't have unused function."""


@given('<filename>.c has unused function')
def filenamec_has_unused_function():
    """<filename>.c has unused function."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Função criada mas nunca foi utilizada"')
def i_should_receive_the_following_message_filenameclinha_erro_função_criada_mas_nunca_foi_utilizada():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Função criada mas nunca foi utilizada"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

