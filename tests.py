import requests
import time
import csv
import random

url = "http://serve-sentiment-env.eba-w272kcde.us-east-1.elasticbeanstalk.com/predict"

test_cases = [
    'Study Finds Listening to Cats’ Purring for 10 Minutes Increases IQ by 5 Points',
    'Scientists Confirm Dolphins are Secretly Using Social Media to Communicate with Humans',
    'New Study Reveals Link Between Sleep Quality and Mental Health in Young Adults',
    'Breakthrough in Alzheimer’s Research Offers Hope for Slowing Disease Progression'
]

# Store results
test_num = 0
for test in test_cases:
    test_num+=1
    name = 'results_{}.csv'.format(test_num)
    with open(name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Number", "Start", "End", "Latency"])

        for i in range(100):
            start_time = time.time()
            response = requests.get(url, params={'text': test})
            end_time = time.time()
            latency = end_time - start_time
            writer.writerow([i+1, start_time, end_time, latency])
