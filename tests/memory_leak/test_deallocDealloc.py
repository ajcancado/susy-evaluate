# coding=utf-8
"""Dealloc Dealloc feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak/deallocDealloc.feature', 'Code with dealloc dealloc')
def test_code_with_dealloc_dealloc():
    """Code with dealloc dealloc."""


@scenario('memory_leak/deallocDealloc.feature', 'Code without dealloc dealloc')
def test_code_without_dealloc_dealloc():
    """Code without dealloc dealloc."""


@given('<filename>.c doesn't have dealloc dealloc')
def filenamec_doesnt_have_dealloc_dealloc():
    """<filename>.c doesn't have dealloc dealloc."""


@given('<filename>.c has dealloc dealloc')
def filenamec_has_dealloc_dealloc():
    """<filename>.c has dealloc dealloc."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Ponteiro foi liberado duas vezes"')
def i_should_receive_the_following_message_filenameclinha_erro_ponteiro_foi_liberado_duas_vezes():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Ponteiro foi liberado duas vezes"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

