# Local Devices Data Collector

This is a simple script to collect data from local devices in a network.

## Requirements

Installation is needed only if you want to run local web server.

```
pip install -r requirements.txt
```

## Usage

### Collecting data

```
./run.py
```

### View collected data in CLI

```
./api.py
```

```
./api.py serviceName
```

### Run local web server

```
flask --app rest.py run
```

And access the web server at http://localhost:5000, or http://localhost:5000/name/serviceName

### Run systemd service

#### Make service file

```
python make_service.py
```

#### Make sure the service configuration is correct with your OS and yours needs

```
cat local_devices_data_collector.service
```

#### Run the service

```
systemctl --user start local_devices_data_collector.service
```

### Run tests

```
./test.py
```
