# coding=utf-8
"""Unread Variable feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('unused_function_and_variable/unreadVariable.feature', 'Code with unread variable')
def test_code_with_unread_variable():
    """Code with unread variable."""


@scenario('unused_function_and_variable/unreadVariable.feature', 'Code without unread variable')
def test_code_without_unread_variable():
    """Code without unread variable."""


@given('<filename>.c doesn't have unread variable')
def filenamec_doesnt_have_unread_variable():
    """<filename>.c doesn't have unread variable."""


@given('<filename>.c has unread variable')
def filenamec_has_unread_variable():
    """<filename>.c has unread variable."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Atribuição de valor à variável mas nunca utilizado"')
def i_should_receive_the_following_message_filenameclinha_erro_atribuição_de_valor_à_variável_mas_nunca_utilizado():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Atribuição de valor à variável mas nunca utilizado"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

