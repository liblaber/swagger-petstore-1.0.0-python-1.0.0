# ValidationService

A list of all methods in the `ValidationService` service. Click on the method name to view detailed information about that method.

| Methods                           | Description |
| :-------------------------------- | :---------- |
| [get_primitives](#get_primitives) |             |

## get_primitives

- HTTP Method: `GET`
- Endpoint: `/validation/primitives`

**Parameters**

| Name                                | Type  | Required | Description                                               |
| :---------------------------------- | :---- | :------- | :-------------------------------------------------------- |
| min_max_integer                     | int   | ✅       | An integer with min -10 and max 10                        |
| min_max_number                      | float | ✅       | An number with min -1 and max 1                           |
| min_max_length_string               | str   | ✅       | A string with minimum length of 2 and maximum length of 8 |
| string_with_pattern                 | str   | ✅       | A string with a pattern (email format)                    |
| description_in_schema               | str   | ✅       | This desription comes from the schema                     |
| description_in_parameter_and_schema | str   | ✅       | This description comes from the parameter                 |

**Return Type**

`GetParameterlessOkResponse`

**Example Usage Code Snippet**

```python
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
