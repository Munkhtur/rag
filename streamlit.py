import streamlit as st
import requests

def main():
    st.title("Mongolian QA System")
    query = st.text_input("Enter your query:")
    
    if st.button("Submit"):
        with st.spinner("Processing..."):
            response = requests.post("http://127.0.0.1:8000/query", json={"query": query})
            if response.status_code == 200:
                data = response.json()
                # st.subheader("Relevant Documents")
                # for i, doc in enumerate(data["relevant_documents"], 1):
                #     st.markdown(f"**Document {i}:** {doc}")
                # st.subheader("Generated Response")
                st.write(data["response"])
            else:
                st.error("Failed to fetch response from the server.")

if __name__ == "__main__":
    main()
