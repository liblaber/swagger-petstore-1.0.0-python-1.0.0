# GeneralService

A list of all methods in the `GeneralService` service. Click on the method name to view detailed information about that method.

| Methods                                                 | Description                         |
| :------------------------------------------------------ |:------------------------------------|
| [get_parameterless](#get_parameterless)                 | Example of parameterless endpoint   |
| [get_only_primitives](#get_only_primitives)             | Example of primitives only endpoint |
| [get_model_and_primitives](#get_model_and_primitives)   |                                     |
| [post_model_and_primitives](#post_model_and_primitives) |                                     |
| [get_arrays_of_primitives](#get_arrays_of_primitives)   |                                     |
| [get_array_of_models](#get_array_of_models)             |                                     |
| [get_one_of](#get_one_of)                               | One of complex models endpoint      |


## get_parameterless

- HTTP Method: `GET`
- Endpoint: `/general/parameterless`

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.general.get_parameterless()

print(result)
```

## get_only_primitives

- HTTP Method: `GET`
- Endpoint: `/general/only-primitives`

**Parameters**

| Name                      | Type  | Required | Description              |
| :------------------------ | :---- | :------- |:-------------------------|
| int_param                 | int   | ✅       |                          |
| string_param              | str   | ✅       | String parameter example |
| number_param              | float | ✅       | Number parameter example |
| bool_param                | bool  | ✅       |                          |
| deprecated_required_param | int   | ✅       |                          |
| deprecated_optional_param | int   | ❌       |                          |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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

## get_model_and_primitives

- HTTP Method: `GET`
- Endpoint: `/general/model-and-primitives`

**Parameters**

| Name         | Type   | Required | Description |
| :----------- | :----- | :------- | :---------- |
| int_param    | int    | ✅       |             |
| person_param | Person | ✅       |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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

## post_model_and_primitives

- HTTP Method: `POST`
- Endpoint: `/general/model-and-primitives`

**Parameters**

| Name         | Type   | Required | Description       |
| :----------- | :----- | :------- | :---------------- |
| request_body | Person | ✅       | The request body. |
| int_param    | int    | ✅       |                   |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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

## get_arrays_of_primitives

- HTTP Method: `GET`
- Endpoint: `/general/arrays-of-primitives`

**Parameters**

| Name                | Type        | Required | Description |
| :------------------ | :---------- | :------- | :---------- |
| int_array_param     | List[int]   | ✅       |             |
| string_array_param  | List[str]   | ✅       |             |
| number_array_param  | List[float] | ✅       |             |
| boolean_array_param | List[bool]  | ✅       |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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

## get_array_of_models

- HTTP Method: `GET`
- Endpoint: `/general/array-of-models`

**Parameters**

| Name         | Type         | Required | Description |
| :----------- | :----------- | :------- | :---------- |
| person_array | List[Person] | ✅       |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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

## get_one_of

- HTTP Method: `GET`
- Endpoint: `/general/one-of`

**Parameters**

| Name                | Type        | Required | Description |
| :------------------ | :---------- | :------- | :---------- |
| car_or_person_param | CarOrPerson | ✅       |             |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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
