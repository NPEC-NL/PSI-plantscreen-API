<h1 align="center"> PSI Plantscreen API implementation
</h1>

<p align="center">
<a href="https://badge.fury.io/py/psi-plantscreen">
<img src="https://badge.fury.io/py/psi-plantscreen.svg" alt="PyPI version"/></a>
</p>

- [Documentation](https://wurDevTim.github.io/PSI-plantscreen-API/) <br>
- [Source Code](https://github.com/wurDevTim/PSI-plantscreen-API) <br>
---

Photon System Instruments (PSI) develivers equipment accross the globe. 
Most of their systems use the plantscreen software, which comes with an API.
This API is tricky to implement. 
The endpoints for instance do not follow the camelCase naming convention, starting the first keyword with a capital.
This causes problems for most dict to dataclass convertors like dataclasses_json. Luckily swagger can handle this. 
The wrapping of the returnbodies with a unique keyword is handles with wrapers.

We, the NPEC team, believe it's a waist of everyones time if we all have to figure out how to get this working.
Therefore we created he swagger file and a simple python wrapper to integrate the plantscreen API.

## Installation 
`pip install psi-plantscreen `  
Build and tested with python 3.8 on windows 10  
Cross platform support for Linux, macOS and Windows

## Example implementation
Uses a .env file with the following fields:
```
URL: <The url or ip-address of your plantscreen machine >
PORT: <Poort on which the plantscreen API is available>
```
The environment files have one additional depency: `pip install python-dotenv`
Examples:
- [Calls to all endpoints](https://github.com/wurDevTim/PSI-plantscreen-API/blob/main/example_implementation.py)
- [How to download the last 5 measurement files](https://github.com/wurDevTim/PSI-plantscreen-API/blob/main/example_usecase.py)

## Contributing
### Build requirements:
build >= 1.0.3
setuptools >= 21.0.0
twine >= 4.0.2
mkdocs >= 1.5.3
mkdocs-material >= 9.5.6


### Updating the swagger file
The API is automatically generated from the [swagger file](https://github.com/wurDevTim/PSI-Fytotron-API/blob/main/swagger_file/PSI_fytotron_API.json) with the [swagger editor](https://editor.swagger.io/).
After generation unpack the zip and move them to the following location:
- Move The `docs` folder to: `docs/Code/Swagger_docs`
- `REAME.md` is copied to: `docs/Code`
- Move the code from `swagger_client` to `plantscreen/swagger_client`. 
    - Replace all occurances of `from swagger_client` with `from plantscreen.swagger_client`
    - When no datetimes is set, PSI returns an empty string by default. The swagger conversion throws a valueerror when it tries to convert this empty string to a datetime object. To solve this, go to `swagger_client > api_client`, the function: `__deserialize_datatime` and change the return of a ValueError to an empty string.

There are two endpoints with multiple return values. While the keyword: `oneof` is used in the swagger file we did not manage to generate this correctly in February 2024. The current solution is to update the swagger file:

In swagger_client > api > probe_api.py
Function: `probe_with_http_info` updates the call to:
if 'id' in params:
- response_type='JsonProbeByIDResult'
else
- response_type='JsonProbeByResult'

In swagger_client > api > msc_api.py
Function `msc_calibration_light_with_http_info` updates the call to:
if 'id' in params:
- response_type='JsonMscCalibrationLightByIDResult'
else
- response_type='JsonMscCalibrationLightResult'

Additional notes:
- The fileendpoints are called without the '/json' , which means they require a different url.
- It's unclear how to implement streams in the swagger file, therefore the 'file' endpoint is done by hand

### Documentation
Build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

## Authors
Tim van Daalen and Pinglin Zhang
NPEC
https://www.npec.nl/
