import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
# print(response)  # get status of the request, 200 = OK status
# print(response.json())  # get json from the request
# print(response.json()['items'])  # get list of items from the request

for question in response.json()['items']:
    if question['answer_count'] == 0:
        print(question['title'])  # get each question from a list of items
        print(question['link'])  # display link to each stackoverflow question
    else:
        print("Skipped")
    print()
