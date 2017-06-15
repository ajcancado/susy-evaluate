# coding=utf-8
"""Incorrect String Boolean Error feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/incorrectStringBooleanError.feature', 'Code with incorrect string boolean error')
def test_code_with_incorrect_string_boolean_error():
    """Code with incorrect string boolean error."""


@scenario('checking_data_type/incorrectStringBooleanError.feature', 'Code without incorrect string boolean error')
def test_code_without_incorrect_string_boolean_error():
    """Code without incorrect string boolean error."""


@given('<filename>.c doesn't have incorrect string boolean error')
def filenamec_doesnt_have_incorrect_string_boolean_error():
    """<filename>.c doesn't have incorrect string boolean error."""


@given('<filename>.c has incorrect string boolean error')
def filenamec_has_incorrect_string_boolean_error():
    """<filename>.c has incorrect string boolean error."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Conversão literal de variável tipo carácter para booleano sempre é verdadeiro"')
def i_should_receive_the_following_message_filenameclinha_erro_conversão_literal_de_variável_tipo_carácter_para_booleano_sempre_é_verdadeiro():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Conversão literal de variável tipo carácter para booleano sempre é verdadeiro"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

