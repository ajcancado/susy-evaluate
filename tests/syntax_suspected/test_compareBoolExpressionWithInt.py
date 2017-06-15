# coding=utf-8
"""Compare Bool Expression with Integer feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('syntax_suspected/compareBoolExpressionWithInt.feature', 'Code with compare boolen expression with integer')
def test_code_with_compare_boolen_expression_with_integer():
    """Code with compare boolen expression with integer."""


@scenario('syntax_suspected/compareBoolExpressionWithInt.feature', 'Code without compare boolen expression with integer')
def test_code_without_compare_boolen_expression_with_integer():
    """Code without compare boolen expression with integer."""


@given('<filename>.c doesn't have compare boolen expression with integer')
def filenamec_doesnt_have_compare_boolen_expression_with_integer():
    """<filename>.c doesn't have compare boolen expression with integer."""


@given('<filename>.c has compare boolen expression with integer')
def filenamec_has_compare_boolen_expression_with_integer():
    """<filename>.c has compare boolen expression with integer."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Comparação de tipo booleano com tipo inteiro"')
def i_should_receive_the_following_message_filenameclinha_erro_comparação_de_tipo_booleano_com_tipo_inteiro():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Comparação de tipo booleano com tipo inteiro"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

