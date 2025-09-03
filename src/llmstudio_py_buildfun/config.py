"""Config for openai class build."""

from typing import Literal

from pydantic import BaseModel


# Define input to LLM class
class LlmInput(BaseModel):
    """Attributes:
    model_name: LLM Model name to use
    role:  [user, system]
    content: query string
    """
    model_name: str
    role: Literal['user', 'system']
    content: str


def llm_request(client, content: LlmInput):
    """Args:
        client (): OpenAI client
        content: type and input of request

    Returns: response from llm request
    """
    try:
        response = client.chat.completions.create(
            model = content.model_name,
            messages = [

                {"role": content.role, "content": content.content}
            ]
        )
        return response
    except Exception as e:
        print(f"Error getting response\n{e}")

def parse_llm_out(response):
    # print(response.choices[0].message.content)
    return response.choices[0].message.content
