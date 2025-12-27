# import requests

# city = "Delhi"
# url = f"https://wttr.in/{city}?format=j1"

# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     temp = data["current_condition"][0]["temp_C"]
#     condition = data["current_condition"][0]["weatherDesc"][0]["value"]

#     print(f"City: {city}")
#     print(f"Temperature: {temp}°C")
#     print(f"Condition: {condition}")
# else:
#     print("Failed to fetch data")

import requests

city = "Delhi"
url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url, timeout=5)

print("STATUS CODE:", response.status_code)
print("\nTEXT (first 200 chars):")
print(response.text[:200])

print("\nJSON KEYS:")
print(response.json().keys())
