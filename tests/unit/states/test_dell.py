import pytest
import salt.modules.test as testmod
import saltext.dell.modules.dell_mod as dell_module
import saltext.dell.states.dell_mod as dell_state


@pytest.fixture
def configure_loader_modules():
    return {
        dell_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        dell_state: {
            "__salt__": {
                "dell.example_function": dell_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'dell.example_function' returned: '{echo_str}'",
    }
    assert dell_state.exampled(echo_str) == expected
