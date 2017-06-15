# coding=utf-8
"""Unused Allocated Memory feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('unused_function_and_variable/unusedAllocatedMemory.feature', 'Code with unused allocated memory')
def test_code_with_unused_allocated_memory():
    """Code with unused allocated memory."""


@scenario('unused_function_and_variable/unusedAllocatedMemory.feature', 'Code without unused allocated memory')
def test_code_without_unused_allocated_memory():
    """Code without unused allocated memory."""


@given('<filename>.c doesn't have unused allocated memory')
def filenamec_doesnt_have_unused_allocated_memory():
    """<filename>.c doesn't have unused allocated memory."""


@given('<filename>.c has unused allocated memory')
def filenamec_has_unused_allocated_memory():
    """<filename>.c has unused allocated memory."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Recursos de memória alocados nunca foram utilizados"')
def i_should_receive_the_following_message_filenameclinha_erro_recursos_de_memória_alocados_nunca_foram_utilizados():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Recursos de memória alocados nunca foram utilizados"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

