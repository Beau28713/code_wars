from urllib.parse import urlsplit

def domain_name(url):
    result = urlsplit(url)
    for ele in result:
        if "." in ele:
            print(ele)