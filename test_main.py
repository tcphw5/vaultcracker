# Import pytest so that we can use xfail
# q import pytest
# No longer needed after all tests are implmented

# Import all of our testable functions from main.
from main import press_button, which_to_press, dial_to, should_flip


def test_press_button():
    """Test that we'll know when to press the Button Layer button

    Tests press_button function.
    """
    # should return false since 13 is div by 13 and button need not be pressed
    falseDisplay = 13
    # should return true since 14 is not div by 13
    trueDisplay = 14

    assert press_button(falseDisplay) is False
    assert press_button(trueDisplay) is True


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

    # according to sample on website answer should be 'a'
    code = 'elephant'
    assert 'a' == dial_to(vault_state, code)


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

    # first 3 tests are taken from example
    # other 3 tests test the untested labels (MR, B, K)
    has_red = 0
    has_blue = 1
    has_green = 1
    assert should_flip(vault_state, has_red, has_blue, has_green) is True

    has_red = 0
    has_blue = 1
    has_green = 0
    assert should_flip(vault_state, has_red, has_blue, has_green) is True

    has_red = 0
    has_blue = 0
    has_green = 0
    assert should_flip(vault_state, has_red, has_blue, has_green) is False

    # False because there is no B in serial number
    has_red = 1
    has_blue = 0
    has_green = 1
    assert should_flip(vault_state, has_red, has_blue, has_green) is False

    # False because Maintenance Req light is off
    has_red = 0
    has_blue = 0
    has_green = 1
    assert should_flip(vault_state, has_red, has_blue, has_green) is False

    # True because there is a K in serial number
    has_red = 1
    has_blue = 1
    has_green = 0
    assert should_flip(vault_state, has_red, has_blue, has_green) is True
