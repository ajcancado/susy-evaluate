# coding=utf-8
"""Unused Variable feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('unused_function_and_variable/unusedVariable.feature', 'Code with unused Variable')
def test_code_with_unused_variable():
    """Code with unused Variable."""


@scenario('unused_function_and_variable/unusedVariable.feature', 'Code without unused Variable')
def test_code_without_unused_variable():
    """Code without unused Variable."""


@given('<filename>.c doesn't have unused Variable')
def filenamec_doesnt_have_unused_variable():
    """<filename>.c doesn't have unused Variable."""


@given('<filename>.c has unused Variable')
def filenamec_has_unused_variable():
    """<filename>.c has unused Variable."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável nunca foi utilizada"')
def i_should_receive_the_following_message_filenameclinha_erro_variável_nunca_foi_utilizada():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Variável nunca foi utilizada"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

