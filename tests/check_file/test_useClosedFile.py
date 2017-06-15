# coding=utf-8
"""Use Closed File feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('check_file/useClosedFile.feature', 'Code with use closed file')
def test_code_with_use_closed_file():
    """Code with use closed file."""


@scenario('check_file/useClosedFile.feature', 'Code without use closed file')
def test_code_without_use_closed_file():
    """Code without use closed file."""


@given('<filename>.c doesn't have use closed file')
def filenamec_doesnt_have_use_closed_file():
    """<filename>.c doesn't have use closed file."""


@given('<filename>.c has use closed file')
def filenamec_has_use_closed_file():
    """<filename>.c has use closed file."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Arquivo utilizado que não foi aberto"')
def i_should_receive_the_following_message_filenameclinha_erro_arquivo_utilizado_que_não_foi_aberto():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Arquivo utilizado que não foi aberto"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

