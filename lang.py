from dotenv import dotenv_values

from langchain.chat_models import init_chat_model

userdata = dotenv_values()

llm = init_chat_model(
    model=userdata["MODEL"]
    , base_url=userdata["BASE_URL"]
    , api_key=userdata["CEREBRAS"]
    , temperature=userdata["TEMPERATURE"]
)

risposta = llm.invoke("chi è anders hejlsberg e perchè è importante? rispondi brevemente")


print(risposta.content)