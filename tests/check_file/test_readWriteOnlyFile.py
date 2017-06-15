# coding=utf-8
"""Read Write Only File feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('check_file/readWriteOnlyFile.feature', 'Code with read write only file')
def test_code_with_read_write_only_file():
    """Code with read write only file."""


@scenario('check_file/readWriteOnlyFile.feature', 'Code without read write only file')
def test_code_without_read_write_only_file():
    """Code without read write only file."""


@given('<filename>.c doesn't have read write only file')
def filenamec_doesnt_have_read_write_only_file():
    """<filename>.c doesn't have read write only file."""


@given('<filename>.c has read write only file')
def filenamec_has_read_write_only_file():
    """<filename>.c has read write only file."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de leitura em um arquivo que foi aberto somente para escrita"')
def i_should_receive_the_following_message_filenameclinha_erro_operação_de_leitura_em_um_arquivo_que_foi_aberto_somente_para_escrita():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de leitura em um arquivo que foi aberto somente para escrita"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

