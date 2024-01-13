import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("dell.example_function"),
]


@pytest.fixture
def dell(modules):
    return modules.dell


def test_replace_this_this_with_something_meaningful(dell):
    echo_str = "Echoed!"
    res = dell.example_function(echo_str)
    assert res == echo_str
