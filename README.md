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

Not all endpoints use the default openAPI implementation. for example, file endpoint use a socket (data stream) to download the files. It's unclear how to implement streams in the swagger file. Those endspoints are also called without the returntype prefeix: '/json' , which means they require a different url.
Luckily, openAPi suports the use of mustache template files to customize the generation process. They are used to add the following functionality:
- Custom classes and functionality:
	- `file_api_method.mustache`: file api endpoint used a bytestream instead of an HTTP call to stream the file content.
	- `partial_link_property.mustache`: adds a lazy-loaded property for a direct 1:1 link. When you access it, it calls the related API once, stores the result on the model, and returns the linked object.
	- `partial_implicit_link.mustache`: adds a similar lazy-loaded property, but for links defined at the model level through vendor extensions rather than on a single field. It fetches the related model automatically from the source value on the current object.
	- `partial_rel_function.mustache`: adds a method for relationship lookups that may need extra parameters and may return one object or a list. Unlike the property-based links, this is an explicit function call for more flexible related-data queries.
- `__init__api.mustache`: Allow single value arguments to be passed for parameters accepting a list of values.
- `api_doc.mustache`: Updated the links to other files.
- `api.mustache`: Contains the logic to parse a list of ints for the experiment_id, owner_id and profile_id calls and implements the file_api call.
- `configuration.mustache`: Switches the datetime format to the one passed in the generation command.
- `model_doc.mustache`: Updated to describe relations and links to other files. It is combined with: `generate_docs.py` which genertes documentation for the 'not auto generated' code and lists all models and API endpoints.
- `model_generic.mustache`: adds the custom links and relations mentioned above. Removes the datetime parsing. Additionally a change was added to allow API calls to return 'None', with special logic for 'JsonMscCalibrationLightResult' and 'JsonMscCalibrationLightByIDResult' and the combination of 'JsonProbeResult' and 'JsonProbeByIDResult'. 

More information about mustache templating can be found here: [mustache templates](https://openapi-generator.tech/docs/templating/)
Additionally, a clean set of templates can be generated with the `generate_mustache_templates.yml` workflow. This is ideal to check what was edited or to add new changes.

After this some postprocessing scripts are executed to make it work:
1. run `pip install .` and then use `generate_complete_api_client.py` to create a single file with all the api calls for convenience.
2. Copy `xml_decoder.py` to the plantscreen folder
3. Update the documentation `generate_docs.py` and `update_docs.py`
4. Run `update_init.py` to make the complete_api_client and xml classes available in the package.


### Documentation
Build with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/)

Note, the docs pages will unfortunately not be available untill this repo is made public.
- [complete api](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/CompleteAPIClient.md)
- [XML decoder](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/XMLDecoder.md)
- [API Endpoints](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/API_endpoints.md)
- [Models](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/docs/models.md)
- [example implementations](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_implementation.py)
- [example usecase](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_usecase.py)
