This container uses BioMistral and qdrant vector database that stores the vectors of the contents within datafile. 
Compared to First Container->
1. This uses BioMistral, which is significantly better than Llama.
2. This uses qdrant vector database, before we were using database which is in the same docker image.We were using FAISS Indexed database(so no CRUD operations were possible). But now we can perform CRUD operations on the database because its a docker container which is different from the LLM container. 
Improvements Neededd->
1. Run on GPU for faster inference.
2. Need to play around with Prompt Engineering get better responses. 
Resource I [used](https://www.youtube.com/watch?v=A_m3tCqdts4).
