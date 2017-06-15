# coding=utf-8
"""Invalid Length Modifier Error feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('format_string/invalidLengthModifierError.feature', 'Code with invalid length modifier error')
def test_code_with_invalid_length_modifier_error():
    """Code with invalid length modifier error."""


@scenario('format_string/invalidLengthModifierError.feature', 'Code without invalid length modifier error')
def test_code_without_invalid_length_modifier_error():
    """Code without invalid length modifier error."""


@given('<filename>.c doesn't have invalid length modifier error')
def filenamec_doesnt_have_invalid_length_modifier_error():
    """<filename>.c doesn't have invalid length modifier error."""


@given('<filename>.c has invalid length modifier error')
def filenamec_has_invalid_length_modifier_error():
    """<filename>.c has invalid length modifier error."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Formato de 'string/char*' modificado não pode ser utilizado sem conversão específica"')
def i_should_receive_the_following_message_filenameclinha_erro_formato_de_stringchar_modificado_não_pode_ser_utilizado_sem_conversão_específica():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Formato de 'string/char*' modificado não pode ser utilizado sem conversão específica"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

