# Petstore Python SDK 1.0.0

A Python SDK for Petstore.

- API version: 1.0.0
- SDK version: 1.0.0

## Table of Contents

- [Installation](#installation)
- [Authentication](#authentication)
- [Environments](#environments)
- [Using Union Types in Function Parameters](#using-union-types-in-function-parameters)
- [Services](#services)

## Installation

```bash
pip install petstore
```

## Authentication

### Access Token

The Petstore API uses a access token as a form of authentication.

The access token can be set when initializing the SDK like this:

```py
Petstore(
    access_token="YOUR_ACCESS_TOKEN"
)
```

Or at a later stage:

```py
sdk.set_access_token("YOUR_ACCESS_TOKEN")
```

## Environments

Here is the list of all available environment variables:

```py
production = "https://api.liblab.com"
staging = "https://api-staging.liblab.com"
development = "https://api-dev.liblab.com"
```

Here is how you set an environment:

```py
from petstore import Environment

sdk.set_base_url(Environment.production.value)
```

## Using Union Types in Function Parameters

In Python, a parameter can be annotated with a Union type, indicating it can accept values of multiple types.

### Passing Instances or Dictionaries

When we have a model such as:

```py
ParamType = Union[TypeA, TypeB]
```

utilized in a service as follows

```py
def service_method(param: ParamType):
    # Function implementation
```

You can call `service_method` with an instance of `TypeA`, `TypeB`, or a dictionary that can be converted to an instance of either type.

```python
type_a = TypeA(key="value")
type_b = TypeB(key="value")

sdk.service.service_method(type_a)
sdk.service.service_method(type_b)
sdk.service.service_method({"key": "value"})
```

### Note on Union Instances

You cannot create an instance of a Union type itself. Instead, pass an instance of one of the types in the Union, or a dictionary that can be converted to one of those types.

## Services

A list of all SDK services. Click on the service name to access its corresponding service methods.

| Service                                     |
| :------------------------------------------ |
| [GeneralService](#generalservice)           |
| [ValidationService](#validationservice)     |
| [RequestInputService](#requestinputservice) |
| [MiscService](#miscservice)                 |

### GeneralService

A list of all methods in the `GeneralService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description |
| :------------------------------------------------------ | :---------- |
| [get_parameterless](#get_parameterless)                 |             |
| [get_only_primitives](#get_only_primitives)             |             |
| [get_model_and_primitives](#get_model_and_primitives)   |             |
| [post_model_and_primitives](#post_model_and_primitives) |             |
| [get_arrays_of_primitives](#get_arrays_of_primitives)   |             |
| [get_array_of_models](#get_array_of_models)             |             |
| [get_one_of](#get_one_of)                               |             |

#### **get_parameterless**

- HTTP Method: `GET`
- Endpoint: `/general/parameterless`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------: | :---------- |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.general.get_parameterless()

print(result)
```

#### **get_only_primitives**

- HTTP Method: `GET`
- Endpoint: `/general/only-primitives`

**Parameters**

| Name                      | Type  | Required | Description |
| :------------------------ | :---- | :------: | :---------- |
| int_param                 | int   |    ✅    |             |
| string_param              | str   |    ✅    |             |
| number_param              | float |    ✅    |             |
| bool_param                | bool  |    ✅    |             |
| deprecated_required_param | int   |    ✅    |             |
| deprecated_optional_param | int   |    ❌    |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.general.get_only_primitives(
    int_param=8,
    string_param="stringParam",
    number_param=2.44,
    bool_param=True,
    deprecated_required_param=8,
    deprecated_optional_param=2
)

print(result)
```

#### **get_model_and_primitives**

- HTTP Method: `GET`
- Endpoint: `/general/model-and-primitives`

**Parameters**

| Name         | Type   | Required | Description |
| :----------- | :----- | :------: | :---------- |
| int_param    | int    |    ✅    |             |
| person_param | Person |    ✅    |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment
from petstore.models import Person

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
person_param=Person(
    first_name="firstName",
    last_name="lastName",
    accepted_terms=True,
    age=7,
    address={
        "street": "street",
        "city": "city",
        "number": "number",
        "state": "CA"
    },
    required_deprecated=1
)

result = sdk.general.get_model_and_primitives(
    int_param=3,
    person_param=person_param
)

print(result)
```

#### **post_model_and_primitives**

- HTTP Method: `POST`
- Endpoint: `/general/model-and-primitives`

**Parameters**

| Name         | Type   | Required | Description       |
| :----------- | :----- | :------: | :---------------- |
| request_body | Person |    ✅    | The request body. |
| int_param    | int    |    ✅    |                   |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment
from petstore.models import Person

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = Person(
    first_name="firstName",
    last_name="lastName",
    accepted_terms=True,
    age=7,
    address={
        "street": "street",
        "city": "city",
        "number": "number",
        "state": "CA"
    },
    required_deprecated=1
)

result = sdk.general.post_model_and_primitives(
    request_body=request_body,
    int_param=2
)

print(result)
```

#### **get_arrays_of_primitives**

- HTTP Method: `GET`
- Endpoint: `/general/arrays-of-primitives`

**Parameters**

| Name                | Type        | Required | Description |
| :------------------ | :---------- | :------: | :---------- |
| int_array_param     | List[int]   |    ✅    |             |
| string_array_param  | List[str]   |    ✅    |             |
| number_array_param  | List[float] |    ✅    |             |
| boolean_array_param | List[bool]  |    ✅    |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
int_array_param=[
    8
]
string_array_param=[
    "stringArrayParam"
]
number_array_param=[
    1.18
]
boolean_array_param=[
    False
]

result = sdk.general.get_arrays_of_primitives(
    int_array_param=int_array_param,
    string_array_param=string_array_param,
    number_array_param=number_array_param,
    boolean_array_param=boolean_array_param
)

print(result)
```

#### **get_array_of_models**

- HTTP Method: `GET`
- Endpoint: `/general/array-of-models`

**Parameters**

| Name         | Type         | Required | Description |
| :----------- | :----------- | :------: | :---------- |
| person_array | List[Person] |    ✅    |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
person_array=[
    {
        "first_name": "firstName",
        "last_name": "lastName",
        "accepted_terms": True,
        "age": 7,
        "address": {
            "street": "street",
            "city": "city",
            "number": "number",
            "state": "CA"
        },
        "required_deprecated": 1
    }
]

result = sdk.general.get_array_of_models(person_array=person_array)

print(result)
```

#### **get_one_of**

- HTTP Method: `GET`
- Endpoint: `/general/one-of`

**Parameters**

| Name                | Type        | Required | Description |
| :------------------ | :---------- | :------: | :---------- |
| car_or_person_param | CarOrPerson |    ✅    |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment
from petstore.models.car_or_person import Car

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)
car_or_person_param=Car(
    brand_name="brandName",
    model_name="modelName",
    year=8
)

result = sdk.general.get_one_of(car_or_person_param=car_or_person_param)

print(result)
```

### ValidationService

A list of all methods in the `ValidationService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description |
| :-------------------------------- | :---------- |
| [get_primitives](#get_primitives) |             |

#### **get_primitives**

- HTTP Method: `GET`
- Endpoint: `/validation/primitives`

**Parameters**

| Name                                | Type  | Required | Description                                               |
| :---------------------------------- | :---- | :------: | :-------------------------------------------------------- |
| min_max_integer                     | int   |    ✅    | An integer with min -10 and max 10                        |
| min_max_number                      | float |    ✅    | An number with min -1 and max 1                           |
| min_max_length_string               | str   |    ✅    | A string with minimum length of 2 and maximum length of 8 |
| string_with_pattern                 | str   |    ✅    | A string with a pattern (email format)                    |
| description_in_schema               | str   |    ✅    | This desription comes from the schema                     |
| description_in_parameter_and_schema | str   |    ✅    | This description comes from the parameter                 |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.validation.get_primitives(
    min_max_integer=-1,
    min_max_number=0.41,
    min_max_length_string="sit fug",
    string_with_pattern="ZSKA10@i.8EwXQafpHm6.p0a1Qf.kOU_dOJBIm3.5GKO.HdT8hVl-YQT.N9m5OhS4m.C.le.tjs.MJ.vVO",
    description_in_schema="Amazing",
    description_in_parameter_and_schema="Amazing"
)

print(result)
```

### RequestInputService

A list of all methods in the `RequestInputService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description |
| :---------------------------------------------------- | :---------- |
| [post_strings](#post_strings)                         |             |
| [post_integer](#post_integer)                         |             |
| [post_boolean](#post_boolean)                         |             |
| [post_array_of_primitives](#post_array_of_primitives) |             |
| [post_array_of_objects](#post_array_of_objects)       |             |

#### **post_strings**

- HTTP Method: `POST`
- Endpoint: `/request-input/strings`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------: | :---------------- |
| request_body | str  |    ✅    | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

with open("file.ext", "r") as f:
    request_body = f.read()

result = sdk.request_input.post_strings(request_body=request_body)

print(result)
```

#### **post_integer**

- HTTP Method: `POST`
- Endpoint: `/request-input/integer`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------: | :---------------- |
| request_body | int  |    ✅    | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = 3

result = sdk.request_input.post_integer(request_body=request_body)

print(result)
```

#### **post_boolean**

- HTTP Method: `POST`
- Endpoint: `/request-input/boolean`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------: | :---------------- |
| request_body | bool |    ✅    | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = False

result = sdk.request_input.post_boolean(request_body=request_body)

print(result)
```

#### **post_array_of_primitives**

- HTTP Method: `POST`
- Endpoint: `/request-input/array`

**Parameters**

| Name         | Type      | Required | Description       |
| :----------- | :-------- | :------: | :---------------- |
| request_body | List[str] |    ✅    | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    "do sint"
]

result = sdk.request_input.post_array_of_primitives(request_body=request_body)

print(result)
```

#### **post_array_of_objects**

- HTTP Method: `PUT`
- Endpoint: `/request-input/array`

**Parameters**

| Name         | Type         | Required | Description       |
| :----------- | :----------- | :------: | :---------------- |
| request_body | List[Person] |    ✅    | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    {
        "first_name": "firstName",
        "last_name": "lastName",
        "accepted_terms": True,
        "age": 7,
        "address": {
            "street": "street",
            "city": "city",
            "number": "number",
            "state": "CA"
        },
        "required_deprecated": 1
    }
]

result = sdk.request_input.post_array_of_objects(request_body=request_body)

print(result)
```

### MiscService

A list of all methods in the `MiscService` service. Click on the method name to view detailed information about that method.

| Methods                                                                   | Description |
| :------------------------------------------------------------------------ | :---------- |
| [get_parameterless_with_no_response](#get_parameterless_with_no_response) |             |
| [get_optional_parameters](#get_optional_parameters)                       |             |
| [post_circular_reference](#post_circular_reference)                       |             |

#### **get_parameterless_with_no_response**

- HTTP Method: `GET`
- Endpoint: `/misc/no-response-body`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------: | :---------- |

**Example Usage Code Snippet**

```py
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.misc.get_parameterless_with_no_response()

print(result)
```

#### **get_optional_parameters**

- HTTP Method: `GET`
- Endpoint: `/misc/optional-parameters`

**Parameters**

| Name                  | Type  | Required | Description |
| :-------------------- | :---- | :------: | :---------- |
| optional_int_param    | int   |    ❌    |             |
| optional_string_param | str   |    ❌    |             |
| optional_number_param | float |    ❌    |             |
| optional_bool_param   | bool  |    ❌    |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
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

#### **post_circular_reference**

- HTTP Method: `POST`
- Endpoint: `/misc/circular-reference`

**Parameters**

| Name         | Type                       | Required | Description       |
| :----------- | :------------------------- | :------: | :---------------- |
| request_body | CircularReferenceTestModel |    ✅    | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```py
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
