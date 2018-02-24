import requests
from collections import namedtuple

class Search:
    def __init__(self, limit):
        self.key = "96d05359d76f4e758906539daeab939e"
        self.url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"
        self.limit = limit

    def bing(self, query):
        response = requests.get(self.url,headers={"Ocp-Apim-Subscription-Key":self.key},params={"q":query,"imageType":"Photo"})
        response.raise_for_status()
        return response.json()

    def getThumbs(self, query):
        return [img["thumbnailUrl"] for img in self.bing(query)["value"][:self.limit]]

    def getLinks(self, query):
        return [img["contentUrl"] for img in self.bing(query)["value"][:self.limit]]

    def getLinksAndThumbs(self, query):
        return [namedtuple('Image','thumb, link')._make(image) for image in [[img["thumbnailUrl"],img["contentUrl"]] for img in self.bing(query)["value"][:self.limit]]]
