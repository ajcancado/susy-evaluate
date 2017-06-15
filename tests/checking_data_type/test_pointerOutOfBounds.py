# coding=utf-8
"""Pointer Out Of Bounds feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('checking_data_type/pointerOutOfBounds.feature', 'Code with pointer out of bounds')
def test_code_with_pointer_out_of_bounds():
    """Code with pointer out of bounds."""


@scenario('checking_data_type/pointerOutOfBounds.feature', 'Code without pointer out of bounds')
def test_code_without_pointer_out_of_bounds():
    """Code without pointer out of bounds."""


@given('<filename>.c doesn't have pointer out of bounds')
def filenamec_doesnt_have_pointer_out_of_bounds():
    """<filename>.c doesn't have pointer out of bounds."""


@given('<filename>.c has pointer out of bounds')
def filenamec_has_pointer_out_of_bounds():
    """<filename>.c has pointer out of bounds."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso a posição inválida do ponteiro"')
def i_should_receive_the_following_message_filenameclinha_erro_acesso_a_posição_inválida_do_ponteiro():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Acesso a posição inválida do ponteiro"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

