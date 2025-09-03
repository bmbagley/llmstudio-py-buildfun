"""Config for openai class build."""


from typing import Literal

import lmstudio as lms
from pydantic import BaseModel


# Define input to LLM class
class LlmInput(BaseModel):
    """Class for requesting llm.

    Attributes:
    model_name: LLM Model name to use
    role:  [user, system]
    content: query string
    """
    model_name: str
    role: Literal['user', 'system']
    content: str


def llm_request(client, content: LlmInput):
    """Generate response from llm request.

    Args:
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
    """Func to parse the message from an llm response.

    Args:
        response (): output from openai model json

    Returns: String of llm output

    """
    # print(response.choices[0].message.content)
    return response.choices[0].message.content


def return_downloaded_model(model_type='llm') -> list[lms.AnyDownloadedModel]:
    """Generate list of models downloaded in lmstudio.

    Args:
        model_type (): llm or embedding

    Returns: list of lmstudio models

    """
    dld = lms.list_downloaded_models(namespace=model_type)
    return dld


def user_input_from_list(option_list:list):
    """Function that generates a choose option for users, using a supplied list.

    Args:
        option_list: list of options for a user to choose
    """
    user_input = ''
    input_message = "Type out your option:\n"

    for index, item in enumerate(option_list):
        input_message += f'{index+1}) {item}\n'

    input_message += 'Your choice: '

    while user_input not in map(str, range(1, len(option_list)+1)):
        user_input = input(input_message)
    # while user_input.lower() not in options:
    #     user_input = input(input_message)
    print('You picked: ' + option_list[int(user_input) -1])
