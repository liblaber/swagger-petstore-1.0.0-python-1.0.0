# CircularReferenceTestModel

A model for testing circular references in snippet. It has 2 'Address'es to ensure that the solution won't fail to build two of the same model unless it's an actual circular reference.

**Properties**

| Name         | Type    | Required | Description            |
| :----------- | :------ | :------- |:-----------------------|
| leaf_node    | Node    | ❌       | The leaf node model    |
| home_address | Address | ❌       | The home address model |
| work_address | Address | ❌       | The work address model |
