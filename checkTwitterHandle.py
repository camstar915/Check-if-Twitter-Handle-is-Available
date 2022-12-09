import requests
from win10toast import ToastNotifier

toaster = ToastNotifier()

# Define the Twitter API endpoint for checking if a username is available
API_ENDPOINT = "https://api.twitter.com/i/users/username_available.json"

# Define the Twitter handle you want to check
TWITTER_HANDLE = "ondit"

# Define the parameters to pass to the API endpoint
params = {"username": TWITTER_HANDLE}

# Send a GET request to the API endpoint with the parameters
response = requests.get(API_ENDPOINT, params=params)

# Check the response status code
if response.status_code == 200:
  # If the response is successful, check if the handle is available
  data = response.json()
  if data["valid"] == True:
    # If the handle is available, print a message
    toaster.show_toast("YESSSS IT'S AVAILABLE GRAB IT!!!!!", f"The Twitter handle '{TWITTER_HANDLE}' is available!")
    print(f"The Twitter handle '{TWITTER_HANDLE}' is available!")
  else:
    # If the handle is not available, print a message
    toaster.show_toast("Twitter Handle Not Available", f"The Twitter handle '{TWITTER_HANDLE}' is not available :(")
    print(f"The Twitter handle '{TWITTER_HANDLE}' is not available!")
else:
  # If the response is not successful, print an error message
  print(f"Error: {response.status_code}")
