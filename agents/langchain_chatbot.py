import time

import dotenv
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI  # noqa

dotenv.load_dotenv()


def main():

    tools = [TavilySearchResults(max_results=1)]

    # chat = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    chat = ChatGroq(model="llama3-70b-8192", temperature=0)
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant named Julienne. You may not need to use tools for every query - the user may just want to chat!",
            ),
            MessagesPlaceholder(variable_name="messages"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    agent = create_openai_tools_agent(chat, tools, prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    while True:
        try:
            user_input = input("User input: ")
        except KeyboardInterrupt:
            break

        start = time.perf_counter()
        agent_executor.invoke({"messages": [HumanMessage(content=user_input)]})
        end = time.perf_counter()
        print(f"Execution time: {end - start}")


if __name__ == "__main__":
    main()
