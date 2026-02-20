# XML Decoder Reference

This page documents the functions of the `xml_decoder` module, which is used to parse XML strings from the API into structured data models.

The main function is `parse_xml`, which takes an XML string and returns an instance of the appropriate data model based on the root tag of the XML.

The data models are defined in the `plantscreen.xml_models` package and include classes like `Protocol`, `Configuration`, `GroupTiming`, `DataSet`, and `TAnyShapes`.

Initial tests showed not all fields of the XML are always pressent, as a result we cannot guaranty the parser will always work.

Incase you encouter errors, please check the XML content and make a pull request on the repository so we can improve.

In the meantime and as alternative the xml_to_dict function can be used to convert the XML into a dictionary. This works for any XML.


For example implemenations please see: [example_usecase.py](https://github.com/NPEC-NL/PSI-plantscreen-API/blob/main/example_usecase.py)

[Back to top](#) [Back to API Endpoints](API_endpoints.md) [Back to Models](Models.md) [Back to README](README.md)
