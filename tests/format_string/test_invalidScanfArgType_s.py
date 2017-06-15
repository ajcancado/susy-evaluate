# coding=utf-8
"""Invalid Scanf Argument Type String feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('format_string/invalidScanfArgType_s.feature', 'Code with invalid scanf argument type string')
def test_code_with_invalid_scanf_argument_type_string():
    """Code with invalid scanf argument type string."""


@scenario('format_string/invalidScanfArgType_s.feature', 'Code without invalid scanf argument type string')
def test_code_without_invalid_scanf_argument_type_string():
    """Code without invalid scanf argument type string."""


@given('<filename>.c doesn't have invalid scanf argument type string')
def filenamec_doesnt_have_invalid_scanf_argument_type_string():
    """<filename>.c doesn't have invalid scanf argument type string."""


@given('<filename>.c has invalid scanf argument type string')
def filenamec_has_invalid_scanf_argument_type_string():
    """<filename>.c has invalid scanf argument type string."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Scanf com argumento do tipo 'string/char*' inválido"')
def i_should_receive_the_following_message_filenameclinha_erro_scanf_com_argumento_do_tipo_stringchar_inválido():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Scanf com argumento do tipo 'string/char*' inválido"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

