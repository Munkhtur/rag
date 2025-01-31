from pprint import pprint
from elasticsearch import Elasticsearch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "books", "part_1.txt")
es = Elasticsearch('http://localhost:9200')
client_info = es.info()
print('Connected to Elasticsearch!')
pprint(client_info.body)

index_config = {
    "settings": {
        "analysis": {
            "analyzer": {
                "mongolian_analyzer": {
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
                "analyzer": "mongolian_analyzer"
            }
        }
    }
}

index_name = "documents"

# Create the index (if not already created)
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=index_config)

from elasticsearch.helpers import bulk

# Load and split the document Change this to your file
loader = TextLoader(file_path, encoding="utf-8")
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# Prepare documents for bulk insertion
bulk_data = [
    {
        "_index": index_name,
        "_id": i,
        "_source": {"content": doc.page_content}
    }
    for i, doc in enumerate(docs)
]

# Insert into Elasticsearch
bulk(es, bulk_data)
print("✅ Documents successfully indexed!")