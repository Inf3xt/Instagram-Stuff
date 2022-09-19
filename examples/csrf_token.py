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

# This is the only header needed for now
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}

"""
When making a request for the CSRF token, you should initialise requests with a session.
In this example, I will make two functions for both methods of making a request.
"""

def session():
    with requests.Session() as session:
        response = session.get(
            url="https://www.instagram.com/data/shared_data/",
            headers=headers
        )
        # Here is where the JSON parsing comes in. If you are a noob, please learn dictionaries before this.
        token = response.json()['config']['csrf_token']
        print(token)

def request():
    response = requests.get(
        url="https://www.instagram.com/data/shared_data/",
        headers=headers
    )
    token = response.json()['config']['csrf_token']
    print(token)

# When you run one of these files, you will get a string of letters and numbers.
# Keep this stored in a variable, you'll need this for logging in!