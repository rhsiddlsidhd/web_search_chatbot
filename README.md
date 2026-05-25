# Web Search Chatbot — Tool Use

LLM이 DuckDuckGo 검색 툴을 직접 호출해 질문에 답하는 검색 챗봇.

툴 호출 판단 주체가 코드에서 LLM으로 처음 넘어가는 프로젝트.

## Stack

- Python, LangChain, OpenAI GPT-4.1-mini, Streamlit
- DuckDuckGo Search (langchain-community)

## Run

```bash
uv run streamlit run app.py
```

## Structure

```
web_search_chatbot/
├── app.py        # Streamlit UI + 대화 루프
├── tools.py      # DuckDuckGo 툴 정의
├── agent.py      # LLM bind_tools + 툴 실행 루프
├── prompts.py    # 시스템 프롬프트
└── pyproject.toml
```
