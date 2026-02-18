<h1 align="center"> PSI Plantscreen API implementation
</h1>

<p align="center">
<a href="https://badge.fury.io/py/psi-plantscreen">
<img src="https://badge.fury.io/py/psi-plantscreen.svg" alt="PyPI version"/></a>
</p>

- [Documentation](https://NPEC-NL.github.io/PSI-plantscreen-API/) <br>
- [Source Code](https://github.com/NPEC-NL/PSI-Plantscreen-API) <br>
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
Unfortunately currently only available on test pypi, installable with:
`python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple psi-plantscreen`

`pip install psi-plantscreen `  

## Example implementation
Uses a .env file with the following fields:
```
URL: "http://<ip-address>:<poort>"
```
The environment files have one additional depency: `pip install python-dotenv`
Examples:
- [Calls to all endpoints](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_implementation.py)
- [How to download the last 5 measurement files](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_usecase.py)

## Contributing
We welcome contributions! 
If you encounter bugs, have feature requests, or want to suggest improvements, please [create an issue](https://github.com/NPEC-NL/PSI-plantscreen-API/issues) and provide a clear description.

### Setting up a Development Environment
Requires Python 3.9+
1. **Create a virtual environment (venv):**
	```sh
	python -m venv .venv
	```
2. **Activate the venv:**
	- On Windows:
	  ```sh
	  .venv\Scripts\activate
	  ```
	- On macOS/Linux:
	  ```sh
	  source .venv/bin/activate
	  ```
3. **Install the package with build and test dependencies:**
	```sh
	pip install .[build, test]


### Updating the OpenAPI specification file
The API is automatically generated from the [OpenAPI specification file](https://github.com/NPEC-NL/PSI-Fytotron-API/blob/main/OpenAPI_specification/PSI_fytotron_API.json) with the [openapi generator cli](https://github.com/OpenAPITools/openapi-generator-cli).
The workflows automatically build the client and copy the files to the right folders.
After this some postprocessing scripts are executed to make it work:
1. `fix_field_validator.py` removed the field validators for datetime variables, these don't work.
2. Update the `file` api call with `replace_file_api_file_method.py`, this is not an HTTP endpoint but a socket stream to download files. 
3. run `pip install .` and then use `generate_complete_api_client.py` to create a single file with all the api calls for convenience.
4. Use `fix_one_of_calls.py` to fix the two endpoints with multiple return values. While the keyword: `oneof` is used in the specification, this does not work.
5. Run `simplify_returns.py`, for convenience. 
6. `update_models.py` to account for the `""` the server returns instead of `None` for missing datetime values.
7. `update_config_file.py` to set the datetime format correct.
8. Copy `xml_decoder.py` to the plantscreen folder

Additional notes:
- The fileendpoints are called without the '/json' , which means they require a different url.
- It's unclear how to implement streams in the swagger file, therefore the 'file' endpoint is done by hand

### Documentation
Build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

Note, the docs pages will unfortunately not be available untill this repo is made public.
- [complete api](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/CompleteAPIClient.md)
- [API Endpoints](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/API_endpoints.md)
- [Models](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/models.md)
- [example implementations](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_implementation.py)
- [example usecase](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_usecase.py)
