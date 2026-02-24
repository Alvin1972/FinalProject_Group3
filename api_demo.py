import requests

url = "https://financialmodelingprep.com/stable/search-symbol?query=AAPL&apikey=ujNrC7HZHGpbGGAzjhdKyTq1uLjVaJXJ"          #It asks a website (an API) for data, gets the data back in JSON format, 
response = requests.get(url)                                #converts it into Python data, and prints the first 5 post titles.

print(response)              # Shows the Response object
json_data = response.json()  # Converts response directly into Python objects


print(type(json_data))   # tells you if it's a list or dict
print(json_data)         # shows you the raw structure


# json_data is now a list of dictionaries
#for post in json_data[:5]:
 #   print(post["title"])


#Here are more URL links for APIs:
# https://financialmodelingprep.com/api/v3/dowjones_constituent?apikey=YOUR_API_KEY
#import requests

#url = "https://jsonplaceholder.typicode.com/posts"

#try:
 #   response = requests.get(url, timeout=10)
#    print(response)  # e.g. <Response [200]>

  #  response.raise_for_status()  # Raises HTTPError for bad responses (4xx/5xx)

  #  json_data = response.json()  # Converts response JSON into Python objects

    # json_data is now a list of dictionaries
 #   for post in json_data[:5]:
 #       print(post["title"])

#except requests.exceptions.RequestException as e:
  #  print(f"Request failed: {e}")
#except ValueError as e:

 #   print(f"JSON decoding failed: {e}")
