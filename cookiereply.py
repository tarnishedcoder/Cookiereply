# hello, this is melik cookie tester , you input the range of cookie and you look for specific output :3
import requests

for i in range(25):  # input the number of the range of cookies for search
    cookie = "name={}".format(i)
    headers = {"Cookie": cookie}

    r = requests.get("url input", headers=headers)  # url that youre looking within it
    if (r.status_code == 200) and (
        "text inide the site" in r.text
    ):  # here you look for specific word within the site
        print(r.text)

# this has been made for ctf purposes :3
