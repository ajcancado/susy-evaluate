# coding=utf-8
"""Invalid Print Argument Type Float feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('format_string/invalidPrintArgType_float.feature', 'Code with invalid print argument type float')
def test_code_with_invalid_print_argument_type_float():
    """Code with invalid print argument type float."""


@scenario('format_string/invalidPrintArgType_float.feature', 'Code without invalid print argument type float')
def test_code_without_invalid_print_argument_type_float():
    """Code without invalid print argument type float."""


@given('<filename>.c doesn't have invalid print argument type float')
def filenamec_doesnt_have_invalid_print_argument_type_float():
    """<filename>.c doesn't have invalid print argument type float."""


@given('<filename>.c has invalid print argument type float')
def filenamec_has_invalid_print_argument_type_float():
    """<filename>.c has invalid print argument type float."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento de tipo 'float' é inválido neste caso"')
def i_should_receive_the_following_message_filenameclinha_erro_argumento_de_tipo_float_é_inválido_neste_caso():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento de tipo 'float' é inválido neste caso"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

