# I2C input

|              |                                                                           |
| ------------ | ------------------------------------------------------------------------- |
| name         | i2c input                                                                 |
| version      | v2.0.0                                                                    |
| docker image | [weevenetwork/i2c-input](https://hub.docker.com/r/weevenetwork/i2c-input) |
| tags         | Python, Flask, Docker, Weeve                                              |
| authors      | Ghassen barbouchi                                                         |

***
## Table of Content

- [I2C input](#i2c-input)
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
This module mounts a I2C slave device and reads its data periodically.

### Features
1. Open the connected i2c interface.
2. Read an i2c slave data using the slave address for each period.
3. Forward the data to the next module.

## Environment Variables

### Module Specific
The following module configurations can be provided in a data service designer section on weeve platform:

| Name                 | Environment Variables | Type    | Description                                                                               |
| -------------------- | --------------------- | ------- | ----------------------------------------------------------------------------------------- |
| I2C device path      | I2C_INTERFACE_PATH    | string  | Local path to I2C device                                                                  |
| I2C interface number | I2C_INTERFACE_NUMBER  | integer | The number of the I2C interface. Example : the number of this interface "/dev/i2c-1" is 1 |
| Data Type            | DATA_TYPE             | string  | The data type of incoming data: 'byte' or 'word'                                          |
| Slave Address        | SLAVE_ADDR            | integer | Example : 10 (in hex '0xa')                                                               |
| Offset               | OFFSET                | integer | The address (offset) inside the EEPROM                                                    |
| Polling Period       | PERIOD                | integer | The period between every two successives data receptions                                  |

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
