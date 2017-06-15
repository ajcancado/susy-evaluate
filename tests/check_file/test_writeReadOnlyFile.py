# coding=utf-8
"""Write Read Only File feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('check_file/writeReadOnlyFile.feature', 'Code with write read only file')
def test_code_with_write_read_only_file():
    """Code with write read only file."""


@scenario('check_file/writeReadOnlyFile.feature', 'Code without write read only file')
def test_code_without_write_read_only_file():
    """Code without write read only file."""


@given('<filename>.c doesn't have write read only file')
def filenamec_doesnt_have_write_read_only_file():
    """<filename>.c doesn't have write read only file."""


@given('<filename>.c has write read only file')
def filenamec_has_write_read_only_file():
    """<filename>.c has write read only file."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de escrita em um arquivo que foi aberto somente para leitura"')
def i_should_receive_the_following_message_filenameclinha_erro_operação_de_escrita_em_um_arquivo_que_foi_aberto_somente_para_leitura():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Operação de escrita em um arquivo que foi aberto somente para leitura"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

