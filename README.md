# i2c-input


|              |                                                                                           |
| ------------ | ------------------------------------------------------------------------------------------|
| name         | i2c input                                                                |
| version      | v0.1.0                                                                                    |
| docker image | [weevenetwork/bluetooth-observer-input](https://linktodockerhub/i2c-input) |
| tags         | Python, Flask, Docker, Weeve                                                              |
| authors      | Ghassen barbouchi                                                                         |

***
## Table of Content

- [I2C-ingress](#i2c-input)
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


### Features
1.
2.

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
