# coding=utf-8
"""Unprecise Math Call feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/unpreciseMathCall.feature', 'Code with unprecise math call')
def test_code_with_unprecise_math_call():
    """Code with unprecise math call."""


@scenario('checking_data_type/unpreciseMathCall.feature', 'Code without unprecise math call')
def test_code_without_unprecise_math_call():
    """Code without unprecise math call."""


@given('<filename>.c doesn't have unprecise math call')
def filenamec_doesnt_have_unprecise_math_call():
    """<filename>.c doesn't have unprecise math call."""


@given('<filename>.c has unprecise math call')
def filenamec_has_unprecise_math_call():
    """<filename>.c has unprecise math call."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Passando valor que pode gerar resultado indefinido"')
def i_should_receive_the_following_message_filenameclinha_erro_passando_valor_que_pode_gerar_resultado_indefinido():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Passando valor que pode gerar resultado indefinido"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

