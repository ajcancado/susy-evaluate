# coding=utf-8
"""Possile Buffer Access Out Bounds feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/possileBufferAccessOutBounds.feature', 'Code with possile buffer access out bounds')
def test_code_with_possile_buffer_access_out_bounds():
    """Code with possile buffer access out bounds."""


@scenario('checking_data_type/possileBufferAccessOutBounds.feature', 'Code without possile buffer access out bounds')
def test_code_without_possile_buffer_access_out_bounds():
    """Code without possile buffer access out bounds."""


@given('<filename>.c doesn't have possile buffer access out bounds')
def filenamec_doesnt_have_possile_buffer_access_out_bounds():
    """<filename>.c doesn't have possile buffer access out bounds."""


@given('<filename>.c has possile buffer access out bounds')
def filenamec_has_possile_buffer_access_out_bounds():
    """<filename>.c has possile buffer access out bounds."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso inválido"')
def i_should_receive_the_following_message_filenameclinha_erro_possível_acesso_inválido():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Possível acesso inválido"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

