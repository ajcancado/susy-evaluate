# coding=utf-8
"""Wrong Printf Scanf Parameter Position Error feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('format_string/wrongPrintfScanfParameterPositionError.feature', 'Code with wrong printf scanf parameter position error')
def test_code_with_wrong_printf_scanf_parameter_position_error():
    """Code with wrong printf scanf parameter position error."""


@scenario('format_string/wrongPrintfScanfParameterPositionError.feature', 'Code without wrong printf scanf parameter position error')
def test_code_without_wrong_printf_scanf_parameter_position_error():
    """Code without wrong printf scanf parameter position error."""


@given('<filename>.c doesn't have wrong printf scanf parameter position error')
def filenamec_doesnt_have_wrong_printf_scanf_parameter_position_error():
    """<filename>.c doesn't have wrong printf scanf parameter position error."""


@given('<filename>.c has wrong printf scanf parameter position error')
def filenamec_has_wrong_printf_scanf_parameter_position_error():
    """<filename>.c has wrong printf scanf parameter position error."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Referenciamento de parâmetro foi realizado incorretamente"')
def i_should_receive_the_following_message_filenameclinha_erro_referenciamento_de_parâmetro_foi_realizado_incorretamente():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Referenciamento de parâmetro foi realizado incorretamente"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

