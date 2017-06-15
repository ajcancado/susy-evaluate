# coding=utf-8
"""Mismatch Allocation and Deallocation feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak/mismatchAllocDealloc.feature', 'Code with mismatch allocation and deallocation')
def test_code_with_mismatch_allocation_and_deallocation():
    """Code with mismatch allocation and deallocation."""


@scenario('memory_leak/mismatchAllocDealloc.feature', 'Code without mismatch allocation and deallocation')
def test_code_without_mismatch_allocation_and_deallocation():
    """Code without mismatch allocation and deallocation."""


@given('<filename>.c doesn't have mismatch allocation and deallocation')
def filenamec_doesnt_have_mismatch_allocation_and_deallocation():
    """<filename>.c doesn't have mismatch allocation and deallocation."""


@given('<filename>.c has mismatch allocation and deallocation')
def filenamec_has_mismatch_allocation_and_deallocation():
    """<filename>.c has mismatch allocation and deallocation."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Falta de alocação ou desalocação de memória"')
def i_should_receive_the_following_message_filenameclinha_erro_falta_de_alocação_ou_desalocação_de_memória():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Falta de alocação ou desalocação de memória"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

