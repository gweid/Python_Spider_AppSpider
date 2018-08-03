import csv
import json


def response(flow):
    with open('bilibili.csv', 'a', newline='') as file:
        fieldname = ['title', 'name', 'rname']
        writer = csv.DictWriter(file, fieldnames=fieldname)
        url_1 = 'https://app.bilibili.com/x/v2/region/dynamic/child/list'
        if flow.request.url.startswith(url_1):
            text = flow.response.text
            data = json.loads(text)
            results = data['data']['new']
            for result in results:
                msg = {
                    'title': result['title'],
                    'name': result['name'],
                    'rname': result['rname']
                }
                writer.writerow(msg)
                print(msg)
        url_2 = 'https://app.bilibili.com/x/v2/region/show/child/list'
        if flow.request.url.startswith(url_2):
            text = flow.response.text
            data = json.loads(text)
            results = data['data']
            for result in results:
                msg = {
                    'title': result['title'],
                    'name': result['name'],
                    'rname': result['rname']
                }
                writer.writerow(msg)
                print(msg)
