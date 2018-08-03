import csv
import json
from mitmproxy import ctx


def response(flow):
    url = 'https://api.zhihu.com/topstory/recommend?action=down'
    if flow.request.url.startswith(url):
        text = flow.response.text
        data = json.loads(text)
        msgs = data.get('data')
        for msg in msgs:
            result = msg.get('target')
            with open('zhihu.csv', 'a', newline='') as csvfile:
                filednames = ['title', 'excerpt']
                writer = csv.DictWriter(csvfile, fieldnames=filednames)
                if result:
                    if 'question' in result.keys():
                        data1 = {
                            'title': result['question']['title'],
                            'excerpt': result.get('excerpt')
                        }
                        ctx.log.info(str(data1))
                        writer.writerow(data1)
                    elif 'title' in result.keys():
                        data1 = {
                            'title': result['title'],
                            'excerpt': result['excerpt']
                        }
                        ctx.log.info(str(data1))
                        writer.writerow(data1)
