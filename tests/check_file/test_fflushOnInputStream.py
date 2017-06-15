# coding=utf-8
"""fflush On Input Stream feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('check_file/fflushOnInputStream.feature', 'Code with fflush on input stream')
def test_code_with_fflush_on_input_stream():
    """Code with fflush on input stream."""


@scenario('check_file/fflushOnInputStream.feature', 'Code without fflush on input stream')
def test_code_without_fflush_on_input_stream():
    """Code without fflush on input stream."""


@given('<filename>.c doesn't have fflush on input stream')
def filenamec_doesnt_have_fflush_on_input_stream():
    """<filename>.c doesn't have fflush on input stream."""


@given('<filename>.c has fflush on input stream')
def filenamec_has_fflush_on_input_stream():
    """<filename>.c has fflush on input stream."""


@when('it is submitted to the app')
def it_is_submitted_to_the_app():
    """it is submitted to the app."""


@then('I should receive the following message "[<filename>.c:<linha>]: (erro) Chamada de função fflush() no stream de entrada, podendo resultar em comportamento indefinido em sistemas não-linux"')
def i_should_receive_the_following_message_filenameclinha_erro_chamada_de_função_fflush_no_stream_de_entrada_podendo_resultar_em_comportamento_indefinido_em_sistemas_nãolinux():
    """I should receive the following message "[<filename>.c:<linha>]: (erro) Chamada de função fflush() no stream de entrada, podendo resultar em comportamento indefinido em sistemas não-linux"."""


@then('shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"')
def shows_me_filenamec_nenhum_erro_de_análise_estática_foi_encontrado():
    """shows me "[<filename>.c]: Nenhum erro de análise estática foi encontrado"."""

