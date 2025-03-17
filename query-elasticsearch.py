
from elasticsearch import Elasticsearch
# index_name = "documents"

es = Elasticsearch('http://localhost:9200')
index_name = "tdb"

query = {
    "size": 10,
    "query": {
        "match": {
            "content": "Та ямар зээлийн үйлчилгээтэй вэ?"
        }
    }
}

response = es.search(index=index_name, body=query)

for hit in response["hits"]["hits"]:
    print(f"🔹 {hit['_source']['content']}")