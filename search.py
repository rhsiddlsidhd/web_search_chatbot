from langchain_community.tools import DuckDuckGoSearchResults

search = DuckDuckGoSearchResults(results_separator=';\n')
docs = search.invoke("최근 씨야가 발표한 신곡은 무엇인가요?")

if __name__ == "__main__":
    print(docs)
