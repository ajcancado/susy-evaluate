# coding=utf-8
"""Null Pointer Default Argument feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('null_pointer/nullPointerDefaultArg.feature', 'Code with null pointer default argument')
def test_code_with_null_pointer_default_argument():
    """Code with null pointer default argument."""


@scenario('null_pointer/nullPointerDefaultArg.feature', 'Code without null pointer default argument')
def test_code_without_null_pointer_default_argument():
    """Code without null pointer default argument."""


@given('<filename>.c doesn't have null pointer default argument')
def filenamec_doesnt_have_null_pointer_default_argument():
    """<filename>.c doesn't have null pointer default argument."""


@given('<filename>.c has null pointer default argument')
def filenamec_has_null_pointer_default_argument():
    """<filename>.c has null pointer default argument."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso a pointeiro nulo se o valor padrão foi utilizado"')
def i_should_receive_the_following_message_filenameclinha_erro_possível_acesso_a_pointeiro_nulo_se_o_valor_padrão_foi_utilizado():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso a pointeiro nulo se o valor padrão foi utilizado"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

