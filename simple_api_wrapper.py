import requests


def query_wolfram(query):
    appid = "&appid=LGRV2T-J8R448JUXE"

    query = "?i=" + query.replace(" ", "%20")

    url = "https://api.wolframalpha.com/v1/result" + query + appid
    response = requests.get(url)

    # Converts response to string
    text = response.content.decode("utf-8")

    return text
