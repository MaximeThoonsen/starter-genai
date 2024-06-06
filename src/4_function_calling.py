import json
from pprint import pprint

from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI

from tools import RequestsGetTool

request_get_tool = RequestsGetTool(allow_dangerous_requests=True)
functions = [convert_to_openai_function(request_get_tool)]

llm = ChatOpenAI(model="gpt-4o")

string_or_function_info = llm.invoke("Can you tell me a joke using chucknorris.io?", functions=functions)

if 'function_call' in string_or_function_info.additional_kwargs:
    # get the tool with its name
    tool_name = string_or_function_info.additional_kwargs["function_call"]["name"]
    if tool_name == 'requests_post':
        json_argument = string_or_function_info.additional_kwargs["function_call"]["arguments"]
        arguments = json.loads(json_argument)
        tool_response = request_get_tool.run(arguments)
        response = json.loads(tool_response)
        pprint(response["value"])
else:
    pprint(string_or_function_info.content)
