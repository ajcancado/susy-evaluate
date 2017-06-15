# coding=utf-8
"""Memleak On Realloc feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak/memleakOnRealloc.feature', 'Code with memleak on realloc')
def test_code_with_memleak_on_realloc():
    """Code with memleak on realloc."""


@scenario('memory_leak/memleakOnRealloc.feature', 'Code without memleak on realloc')
def test_code_without_memleak_on_realloc():
    """Code without memleak on realloc."""


@given('<filename>.c doesn't have memleak on realloc')
def filenamec_doesnt_have_memleak_on_realloc():
    """<filename>.c doesn't have memleak on realloc."""


@given('<filename>.c has memleak on realloc')
def filenamec_has_memleak_on_realloc():
    """<filename>.c has memleak on realloc."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de memória no processo de realocação"')
def i_should_receive_the_following_message_filenameclinha_erro_vazamento_de_memória_no_processo_de_realocação():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de memória no processo de realocação"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

