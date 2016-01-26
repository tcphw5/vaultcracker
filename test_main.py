# Import pytest so that we can use xfail
import pytest

# Import all of our testable functions from main.
from main import press_button, which_to_press, dial_to, should_flip


def test_press_button():
    """Test that we'll know when to press the Button Layer button

    Tests press_button function.
    """
    pytest.xfail("Test is not implemented yet.")


def test_which_to_press():
    """Test that we'll know how to respond to the History Layer

    Tests which_to_press function.
    """
    history = []

    for display, expected in [(4, 2), (1, 4), (3, 1), (1, 4), (2, 2)]:
        actual = which_to_press(history, display)
        assert actual == expected
        history.append((display, expected))


def test_dial_to():
    """Test that we'll know how to respond to the Code Layer

    Tests dial_to function.
    """
    vault_state = {
        'serial number': 'XX7e3652',
        'suspicion level': 0,
        'indicators': {
            'maintenance required': False,
            'check engine': True
        },
        'switch count': 6
    }

    pytest.xfail("Test is not implemented yet.")


def test_should_flip():
    """Test that we'll know how to respond to the Switches Layer

    Tests should_flip function.
    """
    vault_state = {
        'serial number': 'FFGXRK89999',
        'suspicion level': 0,
        'indicators': {
            'check engine': True,
            'maintenance required': False
        },
        'switch count': 6
    }

    pytest.xfail("Test is not implemented yet.")
