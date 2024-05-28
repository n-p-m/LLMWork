# LLMContainerization

Developed this repo to keep track of different containerzation techniquest I used my project.

First Container-> Quantized Llama2 which runs on CPU. Goal was to learn how to develop containers for LLM. Need to resolve below issues.

Need to incorporate:

pipenv for piplock
Token length issue. Number of tokens (630) exceeded maximum context length (512). Number of tokens (631) exceeded maximum context length (512). Number of tokens (632) exceeded maximum context length (512). Number of tokens (633) exceeded maximum context length (512). Number of tokens (634) exceeded maximum context length (512).
Its running on CPU, should implement with GPU
Use RAG instead of converstional agent.

Second Container->

This container uses BioMistral and qdrant vector database that stores the vectors of the contents within datafile. Compared to First Container->

This uses BioMistral, which is significantly better than Llama.
This uses qdrant vector database, before we were using database which is in the same docker image.We were using FAISS Indexed database(so no CRUD operations were possible). But now we can perform CRUD operations on the database because its a docker container which is different from the LLM container. Improvements Neededd->
Run on GPU for faster inference.
Need to play around with Prompt Engineering get better responses. Resource I [used](https://www.youtube.com/watch?v=A_m3tCqdts4).
