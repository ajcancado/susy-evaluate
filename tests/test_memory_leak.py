# coding=utf-8
"""Memory leak feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('memory_leak.feature', 'Uninitialized variable analysis')
def test_uninitialized_variable_analysis():
   pass

@given('the code doesn\'t have uninitialized variables')
def the_code_doesnt_have_uninitialized_variables():
    pass


@when('it is submitted to SuSy')
def it_is_submitted_to_susy():
    pass


@then('I shouldn\'t receive any messages')
def i_shouldnt_receive_any_messages():
    pass

