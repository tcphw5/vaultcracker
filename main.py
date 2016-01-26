"""XY77 Battering Ram

A tool for manipulating the backdoor in the XY77 Series Quad-layer Vault.
"""


def read_int():
    """A helper function for reading an integer from stdin

    :return: The integer that was read
    :rtype: int
    """
    return int(input('>> '))


def read_bool():
    """A helper function for reading a bool from stdin.

    Requires that the user type "1" or "0".

    :return: The bool that was read
    :rtype: int
    """
    val = input('>> ')
    while val not in ('1', '0'):
        print("Answer Yes (1) or No (0)")
        val = input('>> ')
    return bool(int(val))


def press_button(display):
    """Returns True if the display value indicates that the button should
    be pressed.

    :param int display: The current value on the Button Layer display

    :return: True if the button should be pressed
    :rtype: bool
    """
    pass


def button_layer(vault_state):
    """Interact with the user to override the Button Layer

    :param vault_state: The current state of the vault

    :return: None
    """
    pass


def which_to_press(history, displayed):
    """Returns the integer value of the button to press in response to the
    button press history and currently displayed value.

    :param list history: A list of pairs (tuples) that represents the
        history of values displayed and buttons pressed. Each tuple
        looks like: (value_displayed, button_pressed)

    :param int displayed: The value that is currently displayed.

    :return: The label of the button to press.
    :rtype: int
    """
    pass


def history_layer(vault_state):
    """Interact with the user to override the History Layer

    :param vault_state: The current state of the vault.

    :return: None
    """
    pass


def dial_to(vault_state, code):
    """Determines which letter to dial to, based on the vault's serial
    number and code word.

    :param vault_state: The current state of the vault.
    :param str code: The code word that is displayed in the Code Layer

    :return: The letter to turn the dial to
    :rtype: str
    """
    pass


def code_layer(vault_state):
    """Interact with the user to override the Code Layer

    :param vault_state: The current state of the vault.

    :return: None
    """
    pass


def should_flip(vault_state, has_red, has_blue, has_green):
    """Determine whether a single switch should be flipped (toggled).

    :param vault_state: The current state of the vault.
    :param bool has_red: True if the red light is on for this switch,
        otherwise False.
    :param bool has_blue: True if the blue light is on for this switch,
        otherwise False.
    :param bool has_green: True if the green light is on for this switch,
        otherwise False.

    :return: True if the user should flip (toggle) this switch, otherwise False
    :rtype: bool
    """
    pass


def switches_layer(vault_state):
    """Interact with the user to override the Switches Layer

    :param vault_state: The current state of the vault.

    :return: None
    """
    pass


def get_vault_state():
    """Interact with the user to create an initial vault state.

    The vault state has several keys:

    * "suspicion level": The vault's current suspicion level (starts at 0).
    * "serial number": The vault's serial number (requires user input).
    * "switch count": The number of switches in the Switches Layer
        (requires user input)
    * "indicators": A dictionary with the following keys:
        * "check engine": True if the vault's Check Engine light is on
            (requires user input)
        * "maintenance required": True if the vault's Maintenance Required
            light is on (requires user input)

    :return: The initial vault state
    :rtype: dict
    """
    state = {
        'suspicion level': 0,
        'indicators': {},
    }

    print("What is the vault's serial number?")
    state['serial number'] = input('>> ')

    print('Is the "check engine" light on?')
    state['indicators']['check engine'] = read_bool()

    print('Is the "maintenance required" light on?')
    state['indicators']['maintenance required'] = read_bool()

    print('How many switches are on the vault?')
    state['switch count'] = read_int()
    return state


def main():
    """Program entry point.

    Greets the user and begins interactive layer override
    guide. Prior to exit, the program warns the user to wait a certain
    amount of time before opening the vault.

    :return: None

    """
    print("Welcome to the XY77 Battering Ram")

    state = get_vault_state()
    print("State acquired. Let's start.")

    print("\n**History Layer**")
    history_layer(state)

    print("\n**Code Layer**")
    code_layer(state)

    print("\n**Switches Layer**")
    switches_layer(state)

    print("\n**Button Layer**")
    button_layer(state)

    print("Layers bypassed.")
    print("Wait", state['suspicion level'],
          "seconds or more to allow suspicion level to dissipate.")


if __name__ == '__main__':
    #  Start it
    main()
