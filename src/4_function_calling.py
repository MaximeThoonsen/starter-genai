import json
from pprint import pprint

from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

from tools import RequestsGetTool


def get_tool(allow_dangerous_requests=False):
    return RequestsGetTool(allow_dangerous_requests=allow_dangerous_requests)


def get_functions(tool):
    return [convert_to_openai_function(tool)]


def get_model(model_name="gpt-4o"):
    return ChatOpenAI(model=model_name)


def invoke_model(model, query, functions=None):
    return model.invoke(query, functions=functions)


def handle_response(response):
    if 'function_call' in response.additional_kwargs:
        tool_name = response.additional_kwargs["function_call"]["name"]
        if tool_name == 'requests_post':
            json_argument = response.additional_kwargs["function_call"]["arguments"]
            arguments = json.loads(json_argument)
            tool_response = get_tool(allow_dangerous_requests=True).run(arguments)
            json_response = json.loads(tool_response)
            pprint(json_response["value"])
    else:
        pprint(response.content)


if __name__ == "__main__":
    tool = get_tool(allow_dangerous_requests=True)
    functions = get_functions(tool)
    model = get_model()
    query = "Can you tell me a joke using chucknorris.io?"
    response = invoke_model(model, query, functions=functions)
    handle_response(response)
