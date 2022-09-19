"""
MIT License

Copyright (c) 2022 Inf3xt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from datetime import datetime
import requests

# This time variable retrieves the current time in epoch format.
# This is needed when you encode the password per Instagram's terms.
time = int(datetime.now().timestamp())

# Header needed for now, but if you have any ideas of dictionaries; you and I know we can add stuff later on.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
password = "password in plain text!"

payload = {
    "username": "your instagram username",
    "enc_password": f"#PWD_INSTAGRAM_BROWSER:0:{time}:{password}" # This formats the password in the way instagram wants it!
}

# If you have just came from csrf_token.py, requests.Session is the way to go!
with requests.Session() as session:
    csrf_token = session.get("https://www.instagram.com/data/shared_data/", headers=headers)
    token = csrf_token.json()

    print(f"CSRF Token in use: {token}")
    
    