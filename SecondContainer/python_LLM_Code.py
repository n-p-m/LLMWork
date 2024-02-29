from langchain import PromptTemplate
from langchain_community.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain_community.embeddings import SentenceTransformerEmbeddings
# from fastapi import FastAPI, Request, Form, Response
# from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates
# from fastapi.staticfiles import StaticFiles
# from fastapi.encoders import jsonable_encoder
from qdrant_client import QdrantClient
from langchain_community.vectorstores import Qdrant
import os
import json


# from prompts_chat_pdf import chat_prompt, CONDENSE_QUESTION_PROMPT


class PDFChatBot:

    def __init__(self):
        # self.data_path = os.path.join('data')
        # self.db_faiss_path = os.path.join('vectordb', 'db_faiss')
        self.local_llm = "BioMistral-7B.Q4_K_M.gguf"

        #self.chat_prompt = PromptTemplate(template=chat_prompt, input_variables=['context', 'question'])
        #self.CONDENSE_QUESTION_PROMPT=CONDENSE_QUESTION_PROMPT

    # def create_vector_db(self):

    #     '''function to create vector db provided the pdf files'''

    #     loader = DirectoryLoader(self.data_path,
    #                          glob='*.pdf',
    #                          loader_cls=PyPDFLoader)

    #     documents = loader.load()
    #     text_splitter = RecursiveCharacterTextSplitter(chunk_size=400,
    #                                                chunk_overlap=50)
    #     texts = text_splitter.split_documents(documents)

    #     embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2',
    #                                    model_kwargs={'device': 'cpu'})

    #     db = FAISS.from_documents(texts, embeddings)
    #     db.save_local(self.db_faiss_path)

    def load_llm(self):
        # Load the locally downloaded model here
        llm = LlamaCpp(
        model_path= self.local_llm,
        temperature=0.3,
        max_tokens=2056,
        top_p=1
        )
        return llm

    def conversational_chain(self,query):
        local_llm = self.load_llm()
        prompt_template = """Use the context information from to generate recommendations for user's question.
        Generate atleast five recommendations to address user's question.
        If you don't know the answer, just say that you don't know, don't try to make up an answer.

        Context: {context}
        Question: {question}

        Only return the helpful answer. Answer must be detailed and well explained.
        Helpful answer:
        """

        embeddings = SentenceTransformerEmbeddings(model_name="NeuML/pubmedbert-base-embeddings")

        url = "http://localhost:6333"

        client = QdrantClient(
            url=url, prefer_grpc=False
        )

        db = Qdrant(client=client, embeddings=embeddings, collection_name="vector_db")

        prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])

        retriever = db.as_retriever(search_kwargs={"k":2})
        chain_type_kwargs = {"prompt": prompt}
        qa = RetrievalQA.from_chain_type(llm=local_llm, chain_type="stuff", retriever=retriever, return_source_documents=True, chain_type_kwargs=chain_type_kwargs, verbose=True)

        return qa(query)

def intialize_chain(query):
    bot = PDFChatBot()
    # bot.create_vector_db()
    conversational_chain = bot.conversational_chain(query)
    return conversational_chain
    # return conversational_chain

query="Anxiety Recommendations."
output=intialize_chain(query)
print("Result->")
print(output['result'])
print("source->")
print(output['source_documents'][0].page_content)
print("document->")
print(output['source_documents'][0].metadata['source'])
# chat_history = []

# conversational_chain = intialize_chain()

# # # Define the context and the question
# # context = ""
# question = "What is machine learning"

# # # Generate the inference
# response = conversational_chain.run(question)

# # Print the response
# print(response)



# async def generateRecommendation():
#     chain = intialize_chain()
#     sentence = "What is machine learning"
#     context = []  # You can add previous conversation context here if any


#     result = await chain.arun(sentence)
#     return result
# print(generateRecommendation())
# await chain.arun("what is over fitting?")
# @cl.on_chat_start
# async def start():
#     msg = cl.Message(content="Starting the bot...")
#     await msg.send()
#     msg.content = "Welcome to Data Science Interview Prep Bot. Ask me your question?"
#     await msg.update()

#     cl.user_session.set("chain", chain)


# @cl.on_message
# async def main(message):
#     chain = cl.user_session.get("chain")
#     cb = cl.AsyncLangchainCallbackHandler(
#         stream_final_answer=False, answer_prefix_tokens=["FINAL", "ANSWER"]
#     )
#     cb.answer_reached = True
#     res = await chain.acall({"question": message, "chat_history": chat_history}, callbacks=[cb])
#     answer = res["answer"]
#     chat_history.append(answer)
#     await cl.Message(content=answer).send()

#     # while(True):
#     #     query = input('User: ')
#     #     response = conversational_chain({"question": query, "chat_history": chat_history})
#     #     chat_history.append(response["answer"])  # Append the answer to chat history
#     #     print(response["answer"])