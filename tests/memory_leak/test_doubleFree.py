# coding=utf-8
"""Double Free feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak/doubleFree.feature', 'Code with double free')
def test_code_with_double_free():
    """Code with double free."""


@scenario('memory_leak/doubleFree.feature', 'Code without double free')
def test_code_without_double_free():
    """Code without double free."""


@given('<filename>.c doesn't have double free')
def filenamec_doesnt_have_double_free():
    """<filename>.c doesn't have double free."""


@given('<filename>.c has double free')
def filenamec_has_double_free():
    """<filename>.c has double free."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Ponteiro foi liberado duas vezes"')
def i_should_receive_the_following_message_filenameclinha_erro_ponteiro_foi_liberado_duas_vezes():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Ponteiro foi liberado duas vezes"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

