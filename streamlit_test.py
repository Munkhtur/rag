import streamlit as st
import random
import time
import requests
import uuid


if "user_id" not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())


st.title("Simple chat " + st.session_state.user_id)


def response_generator(response):

    for word in response.split():
        yield word + " "
        time.sleep(0.05)
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.spinner("Processing..."):
        try:
            response = requests.post("http://127.0.0.1:8000/query", json={"query": prompt, "user_id": st.session_state.user_id})
            if response.status_code == 200:
                data = response.json()
                api_response = data["response"]

                # Display assistant's response
                with st.chat_message("assistant"):
                    st.write_stream(response_generator(api_response))
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": api_response})
            else:
                st.error("Failed to fetch response from the server.")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")





# with st.chat_message("assistant"):
#     response = st.write_stream(response_generator())
# # Add assistant response to chat history
# st.session_state.messages.append({"role": "assistant", "content": response})