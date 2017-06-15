# coding=utf-8
"""Dealloc Return error feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak/deallocret.feature', 'Code with dealloc return error')
def test_code_with_dealloc_return_error():
    """Code with dealloc return error."""


@scenario('memory_leak/deallocret.feature', 'Code without dealloc return error')
def test_code_without_dealloc_return_error():
    """Code without dealloc return error."""


@given('<filename>.c doesn't have dealloc return error')
def filenamec_doesnt_have_dealloc_return_error():
    """<filename>.c doesn't have dealloc return error."""


@given('<filename>.c has dealloc return error')
def filenamec_has_dealloc_return_error():
    """<filename>.c has dealloc return error."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Retorno/acesso de variável já desalocada"')
def i_should_receive_the_following_message_filenameclinha_erro_retornoacesso_de_variável_já_desalocada():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Retorno/acesso de variável já desalocada"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

