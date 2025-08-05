import requests

# Base URL
url = "https://api.thedogapi.com/v1/breeds"

# Your API Key (replace with your actual key from https://thedogapi.com)
api_key = "live_YApFWP26IEK1bWiwFguNUGg7VqBmGUbRIA0OM0JqyzMz2ydcrPrlwNGEzi4HHHmR"

# Headers including the API key
headers = {
    "x-api-key": api_key
}

# Send GET request
response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    breeds = response.json()
    print(f"Retrieved {len(breeds)} breeds.\n")
    # Print the names of the breeds
    for breed in breeds:
        print(breed["name"])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(response.text)

    # checking response code=200 and printing

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
print("\n✅ Status code is 200 OK.")


#Validate json format

try:
    # Send request
    response = requests.get(url, headers=headers)

    response.raise_for_status()

    # Try to parse JSON
    data = response.json()
    
    # If successful, print confirmation and part of the data
    print("\n✅ JSON is valid.")
    print(f"Retrieved {len(data)} items.")

except requests.exceptions.HTTPError as http_err:
    print(f"❌ HTTP error occurred: {http_err}")
except ValueError as json_err:
    print(f"❌ Invalid JSON format: {json_err}")
except Exception as err:
    print(f"❌ Other error: {err}")
    