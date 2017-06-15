# coding=utf-8
"""Invalid Scanf Format Width feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('format_string/invalidScanfFormatWidth.feature', 'Code with invalid scanf format width')
def test_code_with_invalid_scanf_format_width():
    """Code with invalid scanf format width."""


@scenario('format_string/invalidScanfFormatWidth.feature', 'Code without invalid scanf format width')
def test_code_without_invalid_scanf_format_width():
    """Code without invalid scanf format width."""


@given('<filename>.c doesn't have invalid scanf format width')
def filenamec_doesnt_have_invalid_scanf_format_width():
    """<filename>.c doesn't have invalid scanf format width."""


@given('<filename>.c has invalid scanf format width')
def filenamec_has_invalid_scanf_format_width():
    """<filename>.c has invalid scanf format width."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Tamanho da variável no formato 'string/char*' é inválida"')
def i_should_receive_the_following_message_filenameclinha_erro_tamanho_da_variável_no_formato_stringchar_é_inválida():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Tamanho da variável no formato 'string/char*' é inválida"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

