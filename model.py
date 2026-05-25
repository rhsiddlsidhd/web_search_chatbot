from langchain_openai import ChatOpenAI

model = ChatOpenAI(model='gpt-4.1-mini')


if __name__ == "__main__":
    model.invoke("최근 로제가 발표한 신곡은 무엇인가요 ?")