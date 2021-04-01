import requests, os, logging, sys
from gpiozero import DigitalInputDevice
from signal import pause
from dotenv import load_dotenv

load_dotenv(override=True)


def activate():
    state = get_value_from_env("ACTIVATED_STATE")
    send_command(state)


def deactivate():
    state = get_value_from_env("DEACTIVATED_STATE")
    send_command(state)


def get_value_from_env(key):
    value = os.getenv(key)
    if not value:
        logging.error(f"key '{key}' not found in env, process terminated")
        sys.exit(1)
    return value


def send_command(state):
    openhab_thing_url = get_value_from_env("OPENHAB_THING_STATE_URL")
    data = state
    try:
        response = requests.put(openhab_thing_url, data=data)
        logging.debug(f"send command with state '{state}'")
    except:
        logging.warning("request failed")


pin = get_value_from_env("MAGNET_PIN")
magnet = DigitalInputDevice(pin, pull_up=True)

magnet.when_activated = activate
magnet.when_deactivated = deactivate

pause()