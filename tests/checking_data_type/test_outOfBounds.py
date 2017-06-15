# coding=utf-8
"""Out Of Bounds feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/outOfBounds.feature', 'Code with out of bounds')
def test_code_with_out_of_bounds():
    """Code with out of bounds."""


@scenario('checking_data_type/outOfBounds.feature', 'Code without out of bounds')
def test_code_without_out_of_bounds():
    """Code without out of bounds."""


@given('<filename>.c doesn't have out of bounds')
def filenamec_doesnt_have_out_of_bounds():
    """<filename>.c doesn't have out of bounds."""


@given('<filename>.c has out of bounds')
def filenamec_has_out_of_bounds():
    """<filename>.c has out of bounds."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso inválido"')
def i_should_receive_the_following_message_filenameclinha_erro_acesso_inválido():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso inválido"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

