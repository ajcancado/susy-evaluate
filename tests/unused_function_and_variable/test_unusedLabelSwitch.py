# coding=utf-8
"""Unused Label Switch feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('unused_function_and_variable/unusedLabelSwitch.feature', 'Code with unused label switch')
def test_code_with_unused_label_switch():
    """Code with unused label switch."""


@scenario('unused_function_and_variable/unusedLabelSwitch.feature', 'Code without unused label switch')
def test_code_without_unused_label_switch():
    """Code without unused label switch."""


@given('<filename>.c doesn't have unused label switch')
def filenamec_doesnt_have_unused_label_switch():
    """<filename>.c doesn't have unused label switch."""


@given('<filename>.c has unused label switch')
def filenamec_has_unused_label_switch():
    """<filename>.c has unused label switch."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Label não utilizado"')
def i_should_receive_the_following_message_filenameclinha_erro_label_não_utilizado():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Label não utilizado"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

