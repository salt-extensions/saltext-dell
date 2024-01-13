import pytest

pytestmark = [
    pytest.mark.requires_salt_states("dell.exampled"),
]


@pytest.fixture
def dell(states):
    return states.dell


def test_replace_this_this_with_something_meaningful(dell):
    echo_str = "Echoed!"
    ret = dell.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
