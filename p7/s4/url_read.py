import urllib.request

def read_site():
    my_req = urllib.request.urlopen("https://chatgpt.com/")
    print(my_req.read())

read_site()