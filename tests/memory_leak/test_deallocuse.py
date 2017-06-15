# coding=utf-8
"""Dealloc Use feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak/deallocuse.feature', 'Code with dealloc use')
def test_code_with_dealloc_use():
    """Code with dealloc use."""


@scenario('memory_leak/deallocuse.feature', 'Code without dealloc use')
def test_code_without_dealloc_use():
    """Code without dealloc use."""


@given('<filename>.c doesn't have dealloc use')
def filenamec_doesnt_have_dealloc_use():
    """<filename>.c doesn't have dealloc use."""


@given('<filename>.c has dealloc use')
def filenamec_has_dealloc_use():
    """<filename>.c has dealloc use."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso a variável já desalocada"')
def i_should_receive_the_following_message_filenameclinha_erro_acesso_a_variável_já_desalocada():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso a variável já desalocada"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

