# coding=utf-8
"""Uninitiazed Struct Member feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('uninitialized_variable/uninitStructMember.feature', 'Code with uninitiazed struct member')
def test_code_with_uninitiazed_struct_member():
    """Code with uninitiazed struct member."""


@scenario('uninitialized_variable/uninitStructMember.feature', 'Code without uninitiazed struct member')
def test_code_without_uninitiazed_struct_member():
    """Code without uninitiazed struct member."""


@given('<filename>.c doesn't have uninitiazed struct member')
def filenamec_doesnt_have_uninitiazed_struct_member():
    """<filename>.c doesn't have uninitiazed struct member."""


@given('<filename>.c has uninitiazed struct member')
def filenamec_has_uninitiazed_struct_member():
    """<filename>.c has uninitiazed struct member."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi inicializada"')
def i_should_receive_the_following_message_filenameclinha_erro_variável_foi_criada_em_uma_struct_mas_não_foi_inicializada():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi inicializada"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

