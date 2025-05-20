# Imports
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent
from langchain_mistralai import ChatMistralAI
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatMistralAI(model="mistral-large-latest", api_key=os.getenv("MISTRALAI_API_KEY"))

# Initialize the server parameters
server_params = StdioServerParameters(
    command="C:\\Program Files\\nodejs\\npx.cmd",   # In Windows, other OS you can use "npx"
    env={
        "API_TOKEN": os.getenv("API_TOKEN"),
        "BROWSER_AUTH": os.getenv("BROWSER_AUTH"),
        "WEB_UNLOCKER_ZONE": os.getenv("WEB_UNLOCKER_ZONE"),
    },
    args=["@brightdata/mcp"],
)

# Define the chat function
async def chat_with_agent():
    # Initialize the client
    async with stdio_client(server_params) as (read, write):
        # Initialize the session
        async with ClientSession(read, write) as session:
            # Initialize the session
            await session.initialize()
            # Load the tools
            tools = await load_mcp_tools(session)
            # Create the agent
            agent = create_react_agent(model, tools)

            # Start conversation history, this is the initial message from the system prompt
            messages = [
                {
                    "role": "system",
                    "content": "You can use multiple tools in sequence to answer complex questions. Think step by step.",
                }
            ]

            # Start the conversation
            print("Type 'exit' or 'quit' to end the chat.")
            while True:
                # Get the user's message
                user_input = input("\nYou: ")

                # Check if the user wants to end the conversation
                if user_input.strip().lower() in {"exit", "quit"}:
                    print("Goodbye!")
                    break

                # Add the user's message to the conversation history
                messages.append({"role": "user", "content": user_input})

                # Invoke the agent with the full message history
                agent_response = await agent.ainvoke({"messages": messages})

                # Get the agent's reply
                ai_message = agent_response["messages"][-1].content
                
                # Add the agent's reply to the conversation history
                messages.append({"role": "system", "content": ai_message})
                
                # Print the agent's reply
                print(f"Agent: {ai_message}")


# Run the chat function
if __name__ == "__main__":
    # Run the chat function asynchronously
    asyncio.run(chat_with_agent())