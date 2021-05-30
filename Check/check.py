from .utils import getUrl
import requests


def check(domain):
    url = "https://who.is/whois/" + domain

    try:
        x = getUrl(url)

        if "No match for" in x.text or "NOT FOUND" in x.text:
            print(f"Avaliable: {domain}\n")
            with open("domain.txt", "a") as write:
                write.write(domain + "\n")
            return True
        else:
            print(f"Unavaliable: {domain}\n")
            return False
    except requests.exceptions.ConnectionError:
        print(f"Error: {domain}\n")
        with open("error.txt", "a") as write:
            write.write(domain + "\n")
    except:
        pass
