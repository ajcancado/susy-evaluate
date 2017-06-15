# coding=utf-8
"""Invalid Print Argument Type Usigned Integer feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('format_string/invalidPrintArgType_uint.feature', 'Code with invalid print argument type usigned integer')
def test_code_with_invalid_print_argument_type_usigned_integer():
    """Code with invalid print argument type usigned integer."""


@scenario('format_string/invalidPrintArgType_uint.feature', 'Code without invalid print argument type usigned integer')
def test_code_without_invalid_print_argument_type_usigned_integer():
    """Code without invalid print argument type usigned integer."""


@given('<filename>.c doesn't have invalid print argument type usigned integer')
def filenamec_doesnt_have_invalid_print_argument_type_usigned_integer():
    """<filename>.c doesn't have invalid print argument type usigned integer."""


@given('<filename>.c has invalid print argument type usigned integer')
def filenamec_has_invalid_print_argument_type_usigned_integer():
    """<filename>.c has invalid print argument type usigned integer."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento de tipo 'unsigned int' é inválido neste caso"')
def i_should_receive_the_following_message_filenameclinha_erro_argumento_de_tipo_unsigned_int_é_inválido_neste_caso():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Argumento de tipo 'unsigned int' é inválido neste caso"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

