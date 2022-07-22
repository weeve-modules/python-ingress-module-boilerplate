# I2C input

|              |                                                               |
| ------------ | --------------------------------------------------------------|
| name         | i2c input                                                     |
| version      | v1.0.0                                                        |
| docker image | [weevenetwork/i2c-input](https://linktodockerhub/i2c-input)   |
| tags         | Python, Flask, Docker, Weeve                                  |
| authors      | Ghassen barbouchi                                             |

***
## Table of Content

- [i2c-input](#i2c-input)
  - [Table of Content](#table-of-content)
  - [Description](#description)
     - [Features](#features)
  - [Environment Variables](#environment-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Output](#output)

***

## Description
The I2C bus,( Inter-Integrated Circuit, "eye-squared-C") alternatively known as I2C or IIC, is a synchronous, multi-controller/multi-target (controller (master)/target(slave)), is a wired communication protocol in which the best feature is easy to integrate a new device (such as gateway, sensor node, sensor ...).
The user should ensure that the chosen hardware i2c interface,which the slave or slaves correctly connected, works fine before testing the module.

### Features
1. Open the connected i2c interface.
2. Read an i2c slave data using the slave address for each period.

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name                | Environment Variables | Type    | Description                                                   |
|---------------------|-----------------------|---------|---------------------------------------------------------------|
| I2C interface number| I2C_INTERFACE_NUMBER  | integer | Exemple : the number of this interface "/dev/i2c-1" is 1      |
| Slave Address       | SLAVE_ADDR            | integer | Exemple : 10 (in hex '0xa')                                   |
| Data Type           | DATA_TYPE             | string  | The data type which a sensor use it 'byte' or 'word'          |
| Period              | PERIOD                | integer | The period between every two successives data receptions      |

Other features required for establishing the inter-container communication between modules in a data service are set by weeve agent.

### Set by the weeve Agent on the edge-node

| Environment Variables | type   | Description                                    |
| --------------------- | ------ | ---------------------------------------------- |
| MODULE_NAME           | string | Name of the module                             |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output) |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module         |

## Dependencies
```
requests==2.27.1
smbus2
```
## Output

Output of this module is:

* JSON body single object, example:
byte example :
```json
{"i2cData": 119}
```
word example :
```json
{"i2cData": 65481}
```
