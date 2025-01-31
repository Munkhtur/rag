from langchain.schema import Document
from langchain_core.retrievers import BaseRetriever
from typing import List

class HybridRetriever:
    def __init__(self, es_client, pinecone_retriever, cohere_reranker, index_name, bm25_k=5, vector_k=5, top_n=5):
        self.es_client = es_client
        self.pinecone_retriever = pinecone_retriever
        self.cohere_reranker = cohere_reranker
        self.index_name = index_name
        self.bm25_k = bm25_k
        self.vector_k = vector_k
        self.top_n = top_n

    def bm25_search(self, query: str) -> List[Document]:
        """Retrieve top BM25 search results from Elasticsearch."""
        es_query = {
            "size": self.bm25_k,
            "query": {
                "match": {"content": query}
            }
        }
        response = self.es_client.search(index=self.index_name, body=es_query)

        return [
            Document(
                page_content=row["_source"]["content"],
                metadata={"score": row["_score"], "source": "BM25"}
            )
            for row in response["hits"]["hits"]
        ]

    def get_relevant_documents(self, query: str) -> List[Document]:
        """Fetch results from BM25 & Vector Search, merge, deduplicate, and rerank."""
        bm25_docs = self.bm25_search(query)
        vector_docs = self.pinecone_retriever.invoke(query)

        # Manually add "Pinecone" as the source to vector results
        for doc in vector_docs:
            doc.metadata["source"] = "Pinecone"

        # Merge results and remove duplicates based on content
        seen_content = set()
        combined_results = []
        for doc in bm25_docs + vector_docs:
            if doc.page_content not in seen_content:
                seen_content.add(doc.page_content)
                combined_results.append(doc)

        # Apply re-ranking  
    
        reranked_results = self.cohere_reranker.compress_documents(combined_results, query)

        return reranked_results[:self.top_n]
