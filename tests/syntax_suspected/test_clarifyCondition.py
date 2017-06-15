# coding=utf-8
"""Clarify Condition feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('syntax_suspected/clarifyCondition.feature', 'Code with clarify condition')
def test_code_with_clarify_condition():
    """Code with clarify condition."""


@scenario('syntax_suspected/clarifyCondition.feature', 'Code without clarify condition')
def test_code_without_clarify_condition():
    """Code without clarify condition."""


@given('<filename>.c doesn't have clarify condition')
def filenamec_doesnt_have_clarify_condition():
    """<filename>.c doesn't have clarify condition."""


@given('<filename>.c has clarify condition')
def filenamec_has_clarify_condition():
    """<filename>.c has clarify condition."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Condição não esta claramente definida"')
def i_should_receive_the_following_message_filenameclinha_erro_condição_não_esta_claramente_definida():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Condição não esta claramente definida"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

