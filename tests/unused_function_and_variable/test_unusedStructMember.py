# coding=utf-8
"""Unused Struct Member feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('unused_function_and_variable/unusedStructMember.feature', 'Code with unused struct member')
def test_code_with_unused_struct_member():
    """Code with unused struct member."""


@scenario('unused_function_and_variable/unusedStructMember.feature', 'Code without unused struct member')
def test_code_without_unused_struct_member():
    """Code without unused struct member."""


@given('<filename>.c doesn't have unused struct member')
def filenamec_doesnt_have_unused_struct_member():
    """<filename>.c doesn't have unused struct member."""


@given('<filename>.c has unused struct member')
def filenamec_has_unused_struct_member():
    """<filename>.c has unused struct member."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi utilizada"')
def i_should_receive_the_following_message_filenameclinha_erro_variável_foi_criada_em_uma_struct_mas_não_foi_utilizada():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Variável foi criada em uma 'struct' mas não foi utilizada"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

