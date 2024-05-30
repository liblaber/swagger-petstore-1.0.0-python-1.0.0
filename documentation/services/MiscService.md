# MiscService

A list of all methods in the `MiscService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description |
| :------------------------------------------------------------------------ | :---------- |
| [get_parameterless_with_no_response](#get_parameterless_with_no_response) |             |
| [get_optional_parameters](#get_optional_parameters)                       |             |
| [post_circular_reference](#post_circular_reference)                       |             |

## get_parameterless_with_no_response

- HTTP Method: `GET`
- Endpoint: `/misc/no-response-body`

**Example Usage Code Snippet**

```python
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.misc.get_parameterless_with_no_response()

print(result)
```

## get_optional_parameters

- HTTP Method: `GET`
- Endpoint: `/misc/optional-parameters`

**Parameters**

| Name                  | Type  | Required | Description |
| :-------------------- | :---- | :------- | :---------- |
| optional_int_param    | int   | ❌       |             |
| optional_string_param | str   | ❌       |             |
| optional_number_param | float | ❌       |             |
| optional_bool_param   | bool  | ❌       |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.misc.get_optional_parameters(
    optional_int_param=8,
    optional_string_param="optionalStringParam",
    optional_number_param=9.45,
    optional_bool_param=True
)

print(result)
```

## post_circular_reference

- HTTP Method: `POST`
- Endpoint: `/misc/circular-reference`

**Parameters**

| Name         | Type                       | Required | Description       |
| :----------- | :------------------------- | :------- | :---------------- |
| request_body | CircularReferenceTestModel | ✅       | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
from petstore import Petstore, Environment
from petstore.models import CircularReferenceTestModel

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CircularReferenceTestModel(
    leaf_node={
        "name": "name",
        "next": {
            "name": "name",
            "previous": {
                "name": "name",
                "other_children": [
                    {
                        "name": "name"
                    }
                ]
            },
            "other_children": [
                {
                    "name": "name",
                    "previous": {
                        "name": "name"
                    }
                }
            ]
        },
        "previous": {
            "name": "name",
            "next": {
                "name": "name",
                "other_children": [
                    {
                        "name": "name"
                    }
                ]
            },
            "other_children": [
                {
                    "name": "name",
                    "next": {
                        "name": "name"
                    }
                }
            ]
        },
        "other_children": [
            {
                "name": "name",
                "next": {
                    "name": "name",
                    "previous": {
                        "name": "name"
                    }
                },
                "previous": {
                    "name": "name",
                    "next": {
                        "name": "name"
                    }
                }
            }
        ]
    },
    home_address={
        "street": "street",
        "city": "city",
        "number": "number",
        "state": "CA"
    },
    work_address={
        "street": "street",
        "city": "city",
        "number": "number",
        "state": "CA"
    }
)

result = sdk.misc.post_circular_reference(request_body=request_body)

print(result)
```
