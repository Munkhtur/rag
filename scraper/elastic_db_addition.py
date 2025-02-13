from pprint import pprint
from elasticsearch import Elasticsearch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os
import json
import glob
from tqdm import tqdm
import uuid
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "data")
es = Elasticsearch('http://localhost:9200')
client_info = es.info()
print('Connected to Elasticsearch!')
pprint(client_info.body)

index_config = {
    "settings": {
        "analysis": {
            "analyzer": {
                "tdb_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "stop"]
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "content": {
                "type": "text",
                "analyzer": "tdb_analyzer"
            }
        }
    }
}

index_name = "tdb"

# Create the index (if not already created)
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=index_config)

from elasticsearch.helpers import bulk

bulk_data = []
file_path = "./data/loan/additional_data.json"


    # topic = os.path.basename(os.path.dirname(file_path))  # Extract topic name from path
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)  # Store data with topic as the key
    for j, d in enumerate(data):
        obj ={
        "_index": index_name,
        "_id": str(uuid.uuid4()) ,
            "_source": {
                "content": d.get("chunk", ""),  # Get chunk, default to empty string if missing
                "source": d.get("source", "")   # Get source, default to empty string if missing
            }
        }
        bulk_data.append(obj)
bulk(es, bulk_data)
print("✅ Documents successfully indexed!")

