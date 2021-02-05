import requests

postData = {
    "name": "joe123",
    "pass": "password1",
    "form_id": "user_login",
    "op": "Log in",
}

loginUrl = "http://www.reddit.com"

session = requests.Session()
response = session.post(loginUrl, data=postData)

print(response.text)
print(response.headers)
print(session.cookies)  # The session cookie is stored for subsequent requests
