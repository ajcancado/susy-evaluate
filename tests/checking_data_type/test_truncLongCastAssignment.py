# coding=utf-8
"""Truncated Long Cast Assignment feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/truncLongCastAssignment.feature', 'Code with truncated long cast assignment')
def test_code_with_truncated_long_cast_assignment():
    """Code with truncated long cast assignment."""


@scenario('checking_data_type/truncLongCastAssignment.feature', 'Code without truncated long cast assignment')
def test_code_without_truncated_long_cast_assignment():
    """Code without truncated long cast assignment."""


@given('<filename>.c doesn't have truncated long cast assignment')
def filenamec_doesnt_have_truncated_long_cast_assignment():
    """<filename>.c doesn't have truncated long cast assignment."""


@given('<filename>.c has truncated long cast assignment')
def filenamec_has_truncated_long_cast_assignment():
    """<filename>.c has truncated long cast assignment."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação"')
def i_should_receive_the_following_message_filenameclinha_erro_resultado_inteiro_é_atribuído_a_valor_longo_podendo_ocasionalmente_haver_perda_de_informação():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é atribuído a valor longo, podendo ocasionalmente haver perda de informação"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

