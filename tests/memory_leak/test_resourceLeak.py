# coding=utf-8
"""Resource Leak feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak/resourceLeak.feature', 'Code with resource leak')
def test_code_with_resource_leak():
    """Code with resource leak."""


@scenario('memory_leak/resourceLeak.feature', 'Code without resource leak')
def test_code_without_resource_leak():
    """Code without resource leak."""


@given('<filename>.c doesn't have resource leak')
def filenamec_doesnt_have_resource_leak():
    """<filename>.c doesn't have resource leak."""


@given('<filename>.c has resource leak')
def filenamec_has_resource_leak():
    """<filename>.c has resource leak."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de recursos"')
def i_should_receive_the_following_message_filenameclinha_erro_vazamento_de_recursos():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Vazamento de recursos"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

