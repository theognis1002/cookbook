import requests

data = {
    "name": "joe123",
    "pass": "password1",
    "form_id": "user_login",
    "op": "Log in",
}

login_url = "http://www.reddit.com"

session = requests.Session()
response = session.post(login_url, data=data)

print(response.text)
print(response.headers)
print(session.cookies)  # The session cookie is stored for subsequent requests
