## Multi-Step LLM Research Agent

This repo contains a notebook which has a multi-step research tool making use of multiple agents each of which are equipped with specialized tools for performing their tasks.

The agent will be built using LangGraph and have web-search, RAG search, arXiv search, and CDP SDK functionalities.

Also, there is an ArXiv python scrapper tool so that you can get ArXiv papers if you wish to create your own vector database.

# API Credentials

In the notebook, we will accessing several external APIs for which you will need to create an account and API keys from.

- OpenAI - We will be making use of the GPT-4 LLM. You can get an OpenAI API key here - https://platform.openai.com/
- Pinecone - This will allow you to create a vector database for a RAG tool. You can get a Pinecone account and API key here - https://www.pinecone.io/
- SerpAPI - We will be using SerpAPIs Google search tool. You can get an API here - https://serpapi.com/

# Resources

- OpenAI's documentation - https://platform.openai.com/docs/api-reference/introduction
- OpenAI's prompting guide - https://platform.openai.com/docs/guides/prompt-engineering
- Pinecone's documentation - https://docs.pinecone.io/guides/get-started/overview

Special thanks to James Briggs for inspiring this notebook. Check out his Github here - https://github.com/jamescalam