# coding=utf-8
"""Pointer Arith Boolean feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/pointerArithBool.feature', 'Code with Pointer Arith Boolean')
def test_code_with_pointer_arith_boolean():
    """Code with Pointer Arith Boolean."""


@scenario('checking_data_type/pointerArithBool.feature', 'Code without Pointer Arith Boolean')
def test_code_without_pointer_arith_boolean():
    """Code without Pointer Arith Boolean."""


@given('<filename>.c doesn't have Pointer Arith Boolean')
def filenamec_doesnt_have_pointer_arith_boolean():
    """<filename>.c doesn't have Pointer Arith Boolean."""


@given('<filename>.c has Pointer Arith Boolean')
def filenamec_has_pointer_arith_boolean():
    """<filename>.c has Pointer Arith Boolean."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Valor booleano atribuído a ponteiro"')
def i_should_receive_the_following_message_filenameclinha_erro_valor_booleano_atribuído_a_ponteiro():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Valor booleano atribuído a ponteiro"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

