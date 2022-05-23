import imp
import requests
import json
#import pandas as pd
query = """query{
  mission_races_promise(limit:1000000, offset:0, filters: {})
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
r = requests.post(url, json={'query': query})
print(r)


query2 = """query {
    characters {
    results {
      name
      status
      species
      type
      gender
    }
  }
}"""
url2 = 'https://rickandmortyapi.com/graphql/'
r2 = requests.post(url2, json={'query': query2})
print(r2.text)
