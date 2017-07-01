For api overview and usages, check out [this page](overview.md).

**Note:**

- TODO: Most of the GET APIs support filters
- Do not enter trailing slash in API endpoints

[TOC]

### Authentication

The APIs supports Token Auth.

When using Token auth, each request requires the following headers:

Header        | Value
------------- | ---------------
Content-Type  | application/json
Authorization | Token `<token-string>`


A token is generated on creation of every User. For generating tokens of existing Users in your database,
use the management command by running `python3 manage.py generate_tokens`

In order to initially sign-in, or to get your token for making mock API calls, use the Token API as mentioned below.


#### Token API (Login)

Get Token from username & password.
This is the only API that doesn't require Authorization header, and requires a trailing slash

**Method:** POST (form-data)

**Endpoint:** /user/api-token-auth/

**Payload:**

param name  | type    |
------------|---------|
username    | string  |
password    | string  |

**Response:**

```json
{
  "token": "b0d53ee0c5072dea36b68463f6e22936d4e8ecc8"
}
```
