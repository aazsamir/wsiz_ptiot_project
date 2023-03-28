# Local Devices Data Collector

This is a simple script to collect data from local devices in a network.

## Requirements

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

### Run tests

```
./test.py
```
