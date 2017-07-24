For api overview and usages, check out [this page](overview.md).

**Note:**

- Do not enter trailing slash in API endpoints

[TOC]

## Authentication

The APIs supports Token Auth.

When using Token auth, each request requires the following headers:

 Header        | Value
:--------------|:-----------------------
 Content-Type  | application/json
 Authorization | Token `<token-string>`


A token is generated on creation of every User. For generating tokens of existing Users in your database,
use the management command by running `python3 manage.py generate_tokens`

In order to initially sign-in, or to get your token for making mock API calls, use the Token API as mentioned below.


### Token API

Get Token from username & password.
This is the only API that doesn't require Authorization header, and requires a trailing slash

**Method:** POST [form-data]

**Endpoint:** /api/v1/user/api-token-auth/

**Payload:**

 param name | type
:-----------|:-------
 username   | string
 password   | string

**Response:**

```json
{
  "token": "b0d53ee0c5072dea36b68463f6e22936d4e8ecc8"
}
```

## Quiz

### Question format

 Parameter       | Type    | Description
:----------------|:--------|:-------------------------------------------------
 text            | string  | The text of the question
 quizzes         | array   | A list of labels of all quizzes, the question belongs to<br><br>Needed only if available
 kind            | string  | The type of the accepted format of the answer <br><br> Acceptable values are **MCQ** & **PARAGRAPH**
 required        | boolean | Is the question manadatory to attempt
 editable        | boolean | Can the answer be changed after attempting the question
 choices         | json    | A json of all choices. `choices` has sub-types - `type` & `value`<br><br>Needed only when `kind` is **MCQ**.
 choices.type    | string  | It refers to the choice type. This field denotes how the option will be rendered to the end user. It can be: <li>**TEXT**<br><li>**URL**<br><li>**OTHER** - To be used when you want to give user the choice to enter a value other than those listed in the options.
 choice.value    | string  | The actual value of the option, which is visible to the user
 correct_choices | array   | A list of all the correct choices<br><br>Needed only when `kind` is **MCQ**.


### Add a question

**Method:** POST [raw]

**Endpoint:** /api/v1/question

**Payload:**
As per the *Question Format*

**Sample Request**
```json
{
  "text": "question text",
  "quizzes": ["quiz-label-1"],
  "kind": "MCQ",
  "required": true,
  "editable": true,
  "choices": {
    "1": {
      "value": "sample option 1",
      "type": "TEXT"
    },
    "2": {
      "value": "sample option 2",
      "type": "TEXT"
    },
    "3": {
      "value": "sample option 3",
      "type": "TEXT"
    },
    "4": {
      "value": "sample option 4",
      "type": "TEXT"
    }
  },
  "correct_choices": [
    "1"
  ]
}
```

**Response:**

*201 Created*

```json
{
    "id": "aa858ca8-716e-480b-8ae4-4c9e0373633b",
    "text": "question text",
    "kind": "MCQ",
    "required": true,
    "editable": true,
    "choices": {
        "1": {
            "value": "sample option 1",
            "type": "TEXT"
        },
        "2": {
            "value": "sample option 2",
            "type": "TEXT"
        },
        "3": {
            "value": "sample option 3",
            "type": "TEXT"
        },
        "4": {
            "value": "sample option 4",
            "type": "TEXT"
        }
    },
    "created": "2017-07-24T06:24:47.913773Z",
    "modified": "2017-07-24T06:24:47.913795Z"
}
```


### Add existing questions to a quiz

**Method:** PATCH [raw]

**Endpoint:** /api/v1/quiz/`<quiz_id>`

**Payload:**

 Parameter | Type               | Description
:----------|:-------------------|:---------------------------
 label     | string             | Label of the quiz
 questions | array (of strings) | List of `id`s of questions

**Sample Request**
```json
{
  "label": "quiz-label-1",
  "questions": [
    "952a64bc-21c2-4140-9b07-c28e367e339b",
    "9557de3e-0de0-4496-8b38-7b48c7cc2843",
    "095db37a-6a94-4d2a-b2c9-364d12dbe646"
  ]
}
```

**Response:**

*200 OK*

```json
{
    "id": "fe5f6407-347e-4652-90f5-b13a2a0c75ba",
    "label": "quiz-label-1",
    "questions": [
      "952a64bc-21c2-4140-9b07-c28e367e339b",
      "9557de3e-0de0-4496-8b38-7b48c7cc2843",
      "095db37a-6a94-4d2a-b2c9-364d12dbe646"
    ],
    "created": "2017-07-13T13:08:40.570754Z",
    "modified": "2017-07-24T06:30:33.333765Z"
}
```


### Create/Update a quiz

**Method:** POST [raw]

**Endpoint:** /api/v1/quiz

**Payload:**

 Parameter | Type   | Description
:----------|:-------|:--------------------------------------------------------
 label     | string | Unique label of the quiz. Note that the `label` already exists for every Quiz. Use only pre-existing labels.
 questions | array  | A list of questions (as per the question format)

**Sample Request**
```json
{
  "label": "quiz-label-1",
  "questions": [
    {
      "text": "question text 38",
      "kind": "MCQ",
      "required": true,
      "editable": true,
      "choices": {
        "1": {
          "value": "sample option 1",
          "type": "TEXT"
        },
        "2": {
          "value": "sample option 2",
          "type": "TEXT"
        },
        "3": {
          "value": "sample option 3",
          "type": "TEXT"
        },
        "4": {
          "value": "Please enter the other value",
          "type": "OTHER"
        }
      },
      "correct_choices": [
        "1",
        "2"
      ]
    },
    {
      "text": "question text 39",
      "kind": "MCQ",
      "required": true,
      "editable": true,
      "choices": {
        "1": {
          "value": "sample option 1",
          "type": "TEXT"
        },
        "2": {
          "value": "sample option 2",
          "type": "TEXT"
        },
        "3": {
          "value": "sample option 3",
          "type": "TEXT"
        },
        "4": {
          "value": "Please enter the other value",
          "type": "OTHER"
        }
      },
      "correct_choices": [
        "1",
        "2"
      ]
    }
  ]
}
```

**Response:**

*201 Created*

```json
{
    "id": "fe5f6407-347e-4652-90f5-b13a2a0c75ba",
    "label": "quiz-label-1",
    "questions": [
        {
            "id": "a3dcb4eb-bcbd-4abe-9a72-bb6038f4701a",
            "text": "question text 4",
            "kind": "MCQ",
            "required": true,
            "editable": true,
            "choices": {
                "1": {
                    "type": "TEXT",
                    "value": "sample option 1"
                },
                "2": {
                    "type": "TEXT",
                    "value": "sample option 2"
                },
                "3": {
                    "type": "TEXT",
                    "value": "sample option 3"
                },
                "4": {
                    "type": "TEXT",
                    "value": "sample option 4"
                }
            },
            "created": "2017-07-24T06:22:51.067981Z",
            "modified": "2017-07-24T06:22:51.068009Z"
        },
        {
            "id": "5130d7ff-377a-4525-85d8-1a57f7c7151a",
            "text": "question text 38",
            "kind": "MCQ",
            "required": true,
            "editable": true,
            "choices": {
                "1": {
                    "type": "TEXT",
                    "value": "sample option 1"
                },
                "2": {
                    "type": "TEXT",
                    "value": "sample option 2"
                },
                "3": {
                    "type": "TEXT",
                    "value": "sample option 3"
                },
                "4": {
                    "type": "OTHER",
                    "value": "Please enter the other value"
                }
            },
            "created": "2017-07-24T06:32:54.897477Z",
            "modified": "2017-07-24T06:32:54.897504Z"
        },
        {
            "id": "de6b982c-51c2-4829-bb31-01baf03e64d3",
            "text": "question text 39",
            "kind": "MCQ",
            "required": true,
            "editable": true,
            "choices": {
                "1": {
                    "type": "TEXT",
                    "value": "sample option 1"
                },
                "2": {
                    "type": "TEXT",
                    "value": "sample option 2"
                },
                "3": {
                    "type": "TEXT",
                    "value": "sample option 3"
                },
                "4": {
                    "type": "OTHER",
                    "value": "Please enter the other value"
                }
            },
            "created": "2017-07-24T06:32:54.933292Z",
            "modified": "2017-07-24T06:32:54.933316Z"
        }
    ],
    "created": "2017-07-13T13:08:40.570754Z",
    "modified": "2017-07-24T06:30:33.333765Z"
}
```
