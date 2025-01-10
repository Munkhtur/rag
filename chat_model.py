from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
# from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage

# Setup environment variables and messages
load_dotenv(override=True)

messages = [
SystemMessage(content="Please create various sentence-score pairs in Mongolian based on the context. Result should be in csv format sentence1,sentence2,score. Score is based on its similairty"),
   HumanMessage(content="Дорноговь (монгол бичгээр – дорунагоби) аймаг нь Монгол Улсын зүүн аймаг бөгөөд 1931 онд байгуулагдсан. 2017 оны эцсээр 14 сум, 64 баг, 68606 хүн амтай бөгөөд олон хүн амын тоо хурдацтай нэмэгдэж байгаа юм. Аймгийн төв Сайншанд сум нь улсын нийслэл Улаанбаатар хотоос 450км-т оршдог. Дорноговь аймаг Монгол орны зүүн өмнөд хязгаарт Өмнөговь, Дундговь, Говьсүмбэр, Хэнтий, Сүхбаатар аймгуудтай хил залган оршдог. БНХАУ-тай 600 км- урт газраар хиллэдэг.")

]


# ---- LangChain OpenAI Chat Model Example ----

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o")

# Invoke the model with messages
# result = model.invoke(messages)
# print(f"Answer from OpenAI: {result.content}")


# ---- Anthropic Chat Model Example ----

# Create a Anthropic model
# Anthropic models: https://docs.anthropic.com/en/docs/models-overview
# model = ChatAnthropic(model="claude-3-opus-20240229")

# result = model.invoke(messages)
# print(f"Answer from Anthropic: {result.content}")


# ---- Google Chat Model Example ----

# https://console.cloud.google.com/gen-app-builder/engines
# https://ai.google.dev/gemini-api/docs/models/gemini
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

result = model.invoke(messages)
print(f"Answer from Google: {result.content}")