from elasticsearch import Elasticsearch
import json

try:
    es = Elasticsearch(
        hosts='pl000000sa330',
        http_auth=('YOUR_USERNAME', 'YOUR_PASSWORD'),
        port=9200,
    )
    print '\n', "Connected", json.dumps(es.info())
except Exception as ex:
    print "Error:", ex
    quit()

# print es.search('logstash-2017.03.21')

print '\n', 'Indeksy: '
for index in es.indices.get('*'):
    print index

res = es.search(
    # index='*',
    index='logstash-2017.03.20',
    # body={'query': {'match_all': {}}},
    body={
        'query': {'match': {'_type': 'abpgen-log'}}
    },
    # size=10000
    size=10
    )
print '\n'
print ("Got %d Hits:" %res['hits']['total'])
print '\n'
vi = 0
for hit in res['hits']['hits']:
    # print '\n', hit['_source']
    vi = vi + 1
    # print hit
    print vi,  ': ', json.dumps(hit['_source']['beat']['hostname']), ';', \
                     json.dumps(hit['_source']['@timestamp']), ';', \
                     json.dumps(hit['_source']), ';', '\n', \
                     json.dumps(hit['_source']['message'])