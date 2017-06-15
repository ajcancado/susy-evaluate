# coding=utf-8
"""Truncated Long Cast Return feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/truncLongCastReturn.feature', 'Code with truncated long cast return')
def test_code_with_truncated_long_cast_return():
    """Code with truncated long cast return."""


@scenario('checking_data_type/truncLongCastReturn.feature', 'Code without truncated long cast return')
def test_code_without_truncated_long_cast_return():
    """Code without truncated long cast return."""


@given('<filename>.c doesn't have truncated long cast return')
def filenamec_doesnt_have_truncated_long_cast_return():
    """<filename>.c doesn't have truncated long cast return."""


@given('<filename>.c has truncated long cast return')
def filenamec_has_truncated_long_cast_return():
    """<filename>.c has truncated long cast return."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é retornado como valor longo, podendo ocasionalmente haver perda de informação"')
def i_should_receive_the_following_message_filenameclinha_erro_resultado_inteiro_é_retornado_como_valor_longo_podendo_ocasionalmente_haver_perda_de_informação():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Resultado inteiro é retornado como valor longo, podendo ocasionalmente haver perda de informação"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

