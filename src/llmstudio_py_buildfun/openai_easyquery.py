"""Testing responses from a locally hosted LLM via LMStudio using the OpenAi package."""

from config import LlmInput, llm_request, parse_llm_out
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Dummy key
)
# response = client.chat.completions.create(
#     model="gemma-3-4b-it-qat",
#     messages=[
#         {"role": "user", "content": "Tell me a fun fact about space."}
#     ]
# )
# print(response.choices[0].message.content)


if __name__ == "__main__":
    user_input = input("Type Question: ")
    request_in = LlmInput(model_name="liquid/lfm2-1.2b", role="user", \
                          content=user_input)

    response = llm_request(client, request_in)
    print(parse_llm_out(response))

