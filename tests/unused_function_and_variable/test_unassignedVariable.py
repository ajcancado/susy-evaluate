# coding=utf-8
"""Unassigned Variable feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('unused_function_and_variable/unassignedVariable.feature', 'Code with unassigned variable')
def test_code_with_unassigned_variable():
    """Code with unassigned variable."""


@scenario('unused_function_and_variable/unassignedVariable.feature', 'Code without unassigned variable')
def test_code_without_unassigned_variable():
    """Code without unassigned variable."""


@given('<filename>.c doesn't have unassigned variable')
def filenamec_doesnt_have_unassigned_variable():
    """<filename>.c doesn't have unassigned variable."""


@given('<filename>.c has unassigned variable')
def filenamec_has_unassigned_variable():
    """<filename>.c has unassigned variable."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável não foi atribuída"')
def i_should_receive_the_following_message_filenameclinha_erro_variável_não_foi_atribuída():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Variável não foi atribuída"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

