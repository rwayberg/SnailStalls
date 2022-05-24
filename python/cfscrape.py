#import imp
import requests
import json
import cfscrape
#import pandas as pd
query = """{
  mission_races_promise(limit:100, offset:0, filters: {})
  {
    __typename
    ... on Races{
      all{
        __typename
        ... on Race
        {
          id
          conditions
        }
      }
    }
  }
}"""
url = 'https://api.snailtrail.art/graphql/'
headers = {'accept': '*/*', 'connection': 'keep-alive', 'content-type': 'application/json'}
session = requests.session()
session.headers = headers
scraper = cfscrape.create_scraper(sess=session)
s = scraper.post(url, json={'query': query})
print(s.text)
#r = requests.post(url, json={'query': query}, headers=headers)
#print(r.text)
