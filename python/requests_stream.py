import json
import requests

"""
Download stream of data using Response.iter_lines()
"""
r = requests.get("https://httpbin.org/stream/20", stream=True)

for line in r.iter_lines():
    # filter out keep-alive new lines
    if line:
        decoded_line = line.decode("utf-8")
        print(json.loads(decoded_line))


"""
Download large file by streaming chunks using Response.iter_content() (ie; mp4)
"""

url = "https://files3.lynda.com/secure/courses/786416/VBR_MP4h264_main_SD/786416_00_01_WL30_Batteries.mp4?_JlGPFuqEmh2WYnzy8KqP63YccR5B9TyiaLDUyJqMD8vI0FKsEoIijfxnOyVetNrjDj4fDCUidEarb6NlvSpp8gqOtp4MNS2E_14bhH483Nj8ekt9I0KwkiE6T4k39UnzitRKsZgt55bwl0MhP3aWp1j2U6IsuiqTBssp-Gug0_ZtYFcWvzsH5BN5EsA_A&c3.ri=3775645051486129780"

chunk_size = 256
res = requests.get(url, stream=True)

with open("lynda.mp4", "wb") as f:
    for chunk in res.iter_content(chunk_size=chunk_size):
        f.write(chunk)