<h1 align="center"> PSI Plantscreen API implementation
</h1>

<p align="center">
<a href="https://badge.fury.io/py/psi-plantscreen">
<img src="https://badge.fury.io/py/psi-plantscreen.svg" alt="PyPI version"/></a>
</p>

- [Documentation](https://NPEC-NL.github.io/PSI-plantscreen-API/) <br>
- [Source Code](https://github.com/NPEC-NL/PSI-Plantscreen-API) <br>
---

Photon System Instruments (PSI) delivers equipment across the globe. 
Their cimatecells are controlled with plantscreen software, which comes with an API.
Experience taught us, this API is a bit tricky to implement. 
We believe it's a waste of time if everyone has to figure out how to implement this API and test it.
Therefore, we created the swagger file and a simple python wrapper to integrate the endpoints of the plantscreen API.
Additionally the model classes are enriched with properties and functions to access linked models to make usage easier.

Unfortunately, we were not able to test the 3D scanner and MSC endpoints as the facilities are not equipped with these systems.

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
- [An example of how to download the last 5 measurement files](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_usecase.py)

## Contributing
We welcome contributions! 
If you encounter bugs, have feature requests, or want to suggest improvements, please [create an issue](https://github.com/NPEC-NL/PSI-plantscreen-API/issues) and provide a clear description.

### Setting up a Development Environment
Tested with python 3.10, 3.11, 3.12 and 3.13.


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
6. Copy `xml_decoder.py` to the plantscreen folder
7. Update the documentation `generate_docs.py` and `update_docs.py`

The fileendpoints use a socket (data stream) to download the files. It's unclear how to implement streams in the swagger file, therefore the 'file' endpoint is overwriten with handmade code. Those endspoints are also called without the returntype prefeix: '/json' , which means they require a different url.


### Documentation
Build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

Note, the docs pages will unfortunately not be available untill this repo is made public.
- [complete api](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/CompleteAPIClient.md)
- [XML decoder](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/XMLDecoder.md)
- [API Endpoints](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/API_endpoints.md)
- [Models](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/models.md)
- [example implementations](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_implementation.py)
- [example usecase](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_usecase.py)
