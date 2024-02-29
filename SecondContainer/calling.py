from python_LLM_Code import intialize_chain


sentence="ADHD Inattention Recommendation."

model=intialize_chain()

result=model.run(sentence)
print(result)

