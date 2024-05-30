from petstore import Petstore, Environment

sdk = Petstore(access_token="YOUR_ACCESS_TOKEN", base_url=Environment.DEFAULT.value)

result = sdk.general.get_parameterless()

print(result)
