# Catflap Magnet

Small python application that sends "OPEN" or "CLOSED" state of a magnet sensor to an openHAB Contact Item according to the settings in `.env`.

Please be aware that in my setup the magnet sensor has *no* contact in the default position and is OPEN/"active" when the flap swings so that there is a short contact at the sensor.
Therefore you may be have to switch the state values in the `.env` file according to your setup.

## Setup

0. Install git and pip3
```sh
sudo apt-get update && sudo apt-get install git python3-pip -y
```

1. Clone the Repo
```sh
git clone https://github.com/DarkC35/catflap-magnet
cd catflap-magnet
```

2. Install requirements
```sh
sudo pip3 install -r requirements.txt
```

3. Set required env values
```sh
cp .env.sample .env
nano .env
```
```ini
OPENHAB_THING_STATE_URL=http://<openhab-host>:<openhab-port>/rest/items/<contact-item-name>/state
MAGNET_PIN=<gpio-pin-number>
ACTIVATED_STATE=OPEN
DEACTIVATED_STATE=CLOSED
```

4. Install system unit
```sh
# chmod +x install.sh
./install.sh
```