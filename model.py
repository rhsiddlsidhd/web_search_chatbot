from langchain_openai import ChatOpenAI

model = ChatOpenAI(model='gpt-4.1-mini')
model.invoke("최근 로제가 발표한 신곡은 무엇인가요 ?")