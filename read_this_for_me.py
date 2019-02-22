import requests
import clipboard

print(clipboard.get()) #gets the clipboard text and returns it.

url_to_read = clipboard.get()
url_api = "https://api.meaningcloud.com/summarization-1.0"
payload = "key=[***enter key here***]&url={0}&sentences=5".format(url_to_read)
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url_api, data=payload, headers=headers)
data = response.json()
data = data['summary']
data_to_clipboard = clipboard.set(data)
print('The below text is copied to your clipboard:')
print(data)
