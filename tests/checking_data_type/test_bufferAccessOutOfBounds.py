# coding=utf-8
"""Buffer Access Out Of Bounds feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/bufferAccessOutOfBounds.feature', 'Code with buffer access out Of bounds')
def test_code_with_buffer_access_out_of_bounds():
    """Code with buffer access out Of bounds."""


@scenario('checking_data_type/bufferAccessOutOfBounds.feature', 'Code without buffer access out Of bounds')
def test_code_without_buffer_access_out_of_bounds():
    """Code without buffer access out Of bounds."""


@given('<filename>.c doesn't have buffer access out Of bounds')
def filenamec_doesnt_have_buffer_access_out_of_bounds():
    """<filename>.c doesn't have buffer access out Of bounds."""


@given('<filename>.c has buffer access out Of bounds')
def filenamec_has_buffer_access_out_of_bounds():
    """<filename>.c has buffer access out Of bounds."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Vetor acessado em índice inválido, portanto fora do seu limite"')
def i_should_receive_the_following_message_filenameclinha_erro_vetor_acessado_em_índice_inválido_portanto_fora_do_seu_limite():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Vetor acessado em índice inválido, portanto fora do seu limite"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

