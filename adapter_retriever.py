import random
import torch
from torch import nn
from torch.utils.data import Dataset, DataLoader
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR
from torch.nn.utils import clip_grad_norm_
from sentence_transformers import SentenceTransformer
import chromadb
from langchain_community.vectorstores import Chroma
import os
from langchain.embeddings.base import Embeddings

current_dir = os.path.dirname(os.path.abspath(__file__))
persistent_directory = os.path.join(
    current_dir, "db", "chroma_db_mpnet_try1")

class AdapterEmbeddingFunction(Embeddings):
    def __init__(self, base_model, adapter):
        self.base_model = base_model
        self.adapter = adapter

    def embed_query(self, query):
        # Generate the query embedding using the base model
        query_emb = self.base_model.encode(query, convert_to_tensor=True)
        
        # Apply the adapter to the query embedding
        adapted_query_emb = self.adapter(query_emb)
        
        return adapted_query_emb.cpu().detach().numpy()

    def embed_documents(self, documents):
        # Embed documents without applying the adapter (keep document embeddings as they are)
        return [self.base_model.encode(doc, convert_to_tensor=True).cpu().detach().numpy() for doc in documents]


# Create chroma client
path = "/db/chroma_db_mpnet"
client = chromadb.PersistentClient(path=path)



# Load the base model
base_model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

# def retrieve_documents_embeddings(query_embedding, k=10):
#     query_embedding_list = query_embedding.tolist()

#     results = mongol_collection.query(
#         query_embeddings=[query_embedding_list],
#         n_results=k)
#     return results['documents'][0]

class LinearAdapter(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, input_dim)
    
    def forward(self, x):
        return self.linear(x)
    


def encode_query(query, base_model, adapter):
    device = next(adapter.parameters()).device
    query_emb = base_model.encode(query, convert_to_tensor=True).to(device)
    adapted_query_emb = adapter(query_emb)
    return adapted_query_emb.cpu().detach().numpy()

# torch.device("cpu")
loaded_dict = torch.load('./adapter/linear_adapter_30epochs.pth', map_location=torch.device('cpu'))


# Recreate the adapter
loaded_adapter = LinearAdapter(base_model.get_sentence_embedding_dimension())  # Initialize with appropriate parameters
loaded_adapter.load_state_dict(loaded_dict['adapter_state_dict'])

# Access the training parameters
training_params = loaded_dict['adapter_kwargs']
print(training_params)



adapter_embedding_function = AdapterEmbeddingFunction(base_model, loaded_adapter)

db = Chroma(persist_directory=persistent_directory, embedding_function=adapter_embedding_function)


question ="Дорноговь аймгийн тухай мэдээлэл"

question_embedding = encode_query(question, base_model, loaded_adapter)

        # Retrieve documents using the embedding
retriever = db.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 10}
)


relevant_docs = retriever.invoke(question)

for doc in relevant_docs:
    print(doc)
    print("-------------------")