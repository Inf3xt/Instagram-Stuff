# Introduction

The Instagram API provides a developer a good insite to how a massive web application works. My plan is to provide the knowhow and how to use these APIs that you find in your own applications. If I can do it, you can too - perhaps later on (or if many people want, I can release an awesome tutorial (lol)).

<br>
<br>

# Table of contents
- [Knowledge check!](#knowledge-check)
- [Logging in](#logging-in)
- [Generating CSRF Token](#generating-csrf-token)

# Knowledge check!
Before you continue, make sure you have the following:
- Basic Python knowledge
- Basic JSON knowledge
- The ability to install packages via pip (you can use poetry/conda if that suits your needs better)

# Logging in
This endpoint is where it all starts, you can't do anything without first using this and getting a successful response.

**Base URL** : `https://www.instagram.com`

**Endpoint** : `/accounts/login/ajax/`

**Method** : `POST`

## Request

**Headers required** : 

| Key | Value | Description (if applicable) |
|--------|-----------|-------------|
| User-Agent | Your user agent here! | This is just your user agent. |
| x-csrftoken | XXXXXXX | CSRF Token used for logging in. |
| accept-language | en-US,en;q=0.9 | |
| x-requested-with | XMLHttpRequest | |
| content-type | application/x-www-form-urlencoded | |
| accept | / | |
| referer | https://www.instagram.com/accounts/login%22%7D | |

**Form data** :

| Key | Value | Description |
| ------- | ------------- | ------------------ |
| username | your instagram username | Your Instagram username |
| enc_password | #PWD_INSTAGRAM_BROWSER:0:CurrentEpochTime:PlainTextPassword | One of Instagram's awesome features... |

**type: post form data**

```json
{
    "username": "your username",
    "enc_password": "#PWD_INSTAGRAM_BROWSER:0:CurrentEpochTime:PlainTextPassword"
}
```

## Response

Status code 200:

```jsonc
{
    
}
```

# Generating CSRF Token
Without the CSRF token, you cannot login.

**Base URL** : `https://www.instagram.com`

**Endpoint** : `/data/shared_data/`

**Method** : `GET`

## Request

**Headers required** : 

| Key | Value | Description (if applicable) |
|--------|-----------|-------------|
| User-Agent | Your user agent here! | This is just your user agent. |

## Response

Assuming you get a 200 response:

```jsonc
{
    "config": {
        "csrf_token": "XXXXXXXXXX" // This is what we are after!
    } // Other data can be discarded but it's nice to see all they collect on you.
}
```
