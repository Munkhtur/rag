
from elasticsearch import Elasticsearch
index_name = "documents"

es = Elasticsearch('http://localhost:9200')
ndex_name = "documents"

query = {
    "size": 5,
    "query": {
        "match": {
            "content": "Х. Чойбалсан хэдэн насандаа Санбэйсийн хүрээнд шавилан сууж сахил хүртсэн бэ?"
        }
    }
}

response = es.search(index=index_name, body=query)

for hit in response["hits"]["hits"]:
    print(f"🔹 {hit['_source']['content']}")