# bluetooth-observer-ingress


|              |                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------|
| name         | Bluetooth Observer Ingress                                                                |
| version      | v0.1.0                                                                                    |
| docker image | [weevenetwork/bluetooth-observer-input](https://linktodockerhub/bluetooth-observer-input) |
| tags         | Python, Flask, Docker, Weeve                                                              |
| authors      | Ghassen barbouchi                                                                         |

***
## Table of Content

- [Bluetooth-observer-ingress](#bluetooth-observer-input)
  - [Table of Content](#table-of-content)
  - [Description](#description)
     - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)

***

## Description
BLE:Bluetooth Low Energy
This module use broadcast-advertiser BLE topology mode to scan the BLE devices around it filter the target BLE device by advertised mac address and forward the
manufacturer BLE data to egress module.
The manufacturer data content a structured data composed of sensors values.

### Features
1. Scan ble devices around the host machine.
2. Filter the BLE device by Mac address
3. Forward the advertisement BLE data

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name                | Environment Variables | Type    | Description                                                     |
|---------------------|-----------------------|---------|-----------------------------------------------------------------|
| Scan Timeout        | SCAN_TIMEOUT          | integer | The timeout for the BLE scanning                                |
| Mac Address         | MAC_ADDR              | integer | The advertised mac address of the needed device (sensors device)|
| Period              | PERIOD                | string  | The period between every two successive scans                   |


Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                            |
|-----------------------| ------ | -------------------------------------- |
| EGRESS_URL            | string | HTTP ReST endpoint for the next module |
| MODULE_NAME           | string | Name of the module                     |

## Dependencies
```
requests
python-dotenv
bluepy
```
## Input

Input to this module is:

* JSON body single object, example:

```json
{
    "label-1": 12,
    "label-2": "speed"
}
```

* array of JSON body objects, example:

```json
[
    {
        "Scan Timeout": 3,
        "Mac Address" : "00:10:18:01:4b:b5",
        "Period"      : 5
    }
]
```

## Output

Output of this module is:

* JSON body single object, example:

```json
{
    "bleData": ""
}
```
