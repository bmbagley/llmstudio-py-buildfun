"""Testing responses from a locally hosted LLM via LMStudio using the OpenAi package."""

from openai import OpenAI

from llmstudio_py_buildfun.config import (
    LlmInput,
    llm_request,
    parse_llm_out,
    return_downloaded_model,
    user_input_from_list,
)

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # Dummy key
)


if __name__ == "__main__":
    # Get user input for the Model from a list of downloaded, and the text from the user
    dld_models = return_downloaded_model()
    model_select = user_input_from_list(option_list=[''.join(i.model_key) for i in dld_models])
    user_input = input("Type Question: ")

    # Call specified model with user input
    request_in = LlmInput(model_name=str(model_select), role="user", \
                          content=str(user_input))

    # Return response text only
    response = llm_request(client, request_in)
    print(parse_llm_out(response))

