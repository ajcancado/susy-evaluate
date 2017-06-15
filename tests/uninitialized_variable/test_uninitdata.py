# coding=utf-8
"""Uninitiazed date feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('uninitialized_variable/uninitdata.feature', 'Code with uninitiazed date')
def test_code_with_uninitiazed_date():
    """Code with uninitiazed date."""


@scenario('uninitialized_variable/uninitdata.feature', 'Code without uninitiazed date')
def test_code_without_uninitiazed_date():
    """Code without uninitiazed date."""


@given('<filename>.c doesn't have uninitiazed date')
def filenamec_doesnt_have_uninitiazed_date():
    """<filename>.c doesn't have uninitiazed date."""


@given('<filename>.c has uninitiazed date')
def filenamec_has_uninitiazed_date():
    """<filename>.c has uninitiazed date."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Mémoria foi alocada mas não foi inicializada"')
def i_should_receive_the_following_message_filenameclinha_erro_mémoria_foi_alocada_mas_não_foi_inicializada():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Mémoria foi alocada mas não foi inicializada"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

