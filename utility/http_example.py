import requests

# Enter your code here. Read input from STDIN. Print output to STDOUT

inputId = int(input())
url = "https://jsonmock.doselect.com/api/countries/countries/{0}".format(inputId)
response = requests.get(url)
print(type(response.json()))