# coding=utf-8
"""Float Conversion Overflow feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/floatConversionOverflow.feature', 'Code with float conversion overflow')
def test_code_with_float_conversion_overflow():
    """Code with float conversion overflow."""


@scenario('checking_data_type/floatConversionOverflow.feature', 'Code without float conversion overflow')
def test_code_without_float_conversion_overflow():
    """Code without float conversion overflow."""


@given('<filename>.c doesn't have float conversion overflow')
def filenamec_doesnt_have_float_conversion_overflow():
    """<filename>.c doesn't have float conversion overflow."""


@given('<filename>.c has float conversion overflow')
def filenamec_has_float_conversion_overflow():
    """<filename>.c has float conversion overflow."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow de variável do tipo 'float'"')
def i_should_receive_the_following_message_filenameclinha_erro_overflow_de_variável_do_tipo_float():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Overflow de variável do tipo 'float'"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

