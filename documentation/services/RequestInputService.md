# RequestInputService

A list of all methods in the `RequestInputService` service. Click on the method name to view detailed information about that method.

| Methods                                               | Description |
| :---------------------------------------------------- | :---------- |
| [post_strings](#post_strings)                         |             |
| [post_integer](#post_integer)                         |             |
| [post_boolean](#post_boolean)                         |             |
| [post_array_of_primitives](#post_array_of_primitives) |             |
| [post_array_of_objects](#post_array_of_objects)       |             |

## post_strings

- HTTP Method: `POST`
- Endpoint: `/request-input/strings`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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

## post_integer

- HTTP Method: `POST`
- Endpoint: `/request-input/integer`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | int  | ✅       | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = 3

result = sdk.request_input.post_integer(request_body=request_body)

print(result)
```

## post_boolean

- HTTP Method: `POST`
- Endpoint: `/request-input/boolean`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | bool | ✅       | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
from petstore import Petstore, Environment

sdk = Petstore(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = False

result = sdk.request_input.post_boolean(request_body=request_body)

print(result)
```

## post_array_of_primitives

- HTTP Method: `POST`
- Endpoint: `/request-input/array`

**Parameters**

| Name         | Type      | Required | Description       |
| :----------- | :-------- | :------- | :---------------- |
| request_body | List[str] | ✅       | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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

## post_array_of_objects

- HTTP Method: `PUT`
- Endpoint: `/request-input/array`

**Parameters**

| Name         | Type         | Required | Description       |
| :----------- | :----------- | :------- | :---------------- |
| request_body | List[Person] | ✅       | The request body. |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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
