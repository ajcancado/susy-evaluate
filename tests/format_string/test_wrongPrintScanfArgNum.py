# coding=utf-8
"""Wrong Print Scanf Argument Number feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('format_string/wrongPrintScanfArgNum.feature', 'Code with wrong print scanf argument number')
def test_code_with_wrong_print_scanf_argument_number():
    """Code with wrong print scanf argument number."""


@scenario('format_string/wrongPrintScanfArgNum.feature', 'Code without wrong print scanf argument number')
def test_code_without_wrong_print_scanf_argument_number():
    """Code without wrong print scanf argument number."""


@given('<filename>.c doesn't have wrong print scanf argument number')
def filenamec_doesnt_have_wrong_print_scanf_argument_number():
    """<filename>.c doesn't have wrong print scanf argument number."""


@given('<filename>.c has wrong print scanf argument number')
def filenamec_has_wrong_print_scanf_argument_number():
    """<filename>.c has wrong print scanf argument number."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Número de variáveis utilizadas não corresponde com o número de formatadores"')
def i_should_receive_the_following_message_filenameclinha_erro_número_de_variáveis_utilizadas_não_corresponde_com_o_número_de_formatadores():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Número de variáveis utilizadas não corresponde com o número de formatadores"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

