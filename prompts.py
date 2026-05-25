from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from model import model

question_answering_prompt = ChatPromptTemplate.from_messages(
    [
        (
            'system',
            "아래 context에 기반하여 사용자의 질문에 답변하라:\n\n{context}"
        ),
        MessagesPlaceholder(variable_name='messages')
    ]
)

doc_chain = question_answering_prompt | model