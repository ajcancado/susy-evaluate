from pytest_bdd import scenario, given, when, then
import subprocess 

result = subprocess.check_output('../hello.py silvana', shell=True)

@scenario('hello.feature', 'Say hello')
def test_hello():
    pass

@given("I'm a student user")
def student_user():
    pass

@when("I give my name")
def my_name():
    pass

@then("I should see a message that has hello before my name")
def say_hello():
    global result
    # print(result.stdout)
    assert result.decode('utf-8') == "hello silvana\n"