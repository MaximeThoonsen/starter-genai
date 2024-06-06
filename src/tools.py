import json
from typing import Any, Dict, Optional, Type, Union

from langchain_community.tools import BaseRequestsTool
from langchain_community.tools.requests.tool import _clean_url
from langchain_community.utilities import TextRequestsWrapper
from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field


class RequestsGetToolIInput(BaseModel):
    url: str = Field(..., description="the url to perform the request")


class RequestsGetTool(BaseRequestsTool, BaseTool):
    """Tool for making a POST request to an API endpoint."""

    name: str = "requests_post"
    description: str = """Use this when you want to GET to a website.
    Input should be a json string with one key: "url".
    The value of "url" should be a string
    Be careful to always use double quotes for strings in the json string
    The output will be the text response of the GET request.
    """
    requests_wrapper = TextRequestsWrapper()
    args_schema: Type[
        BaseModel] = RequestsGetToolIInput  # This is what is used to create the function schema for openai

    def _run(
            self, url: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> Union[str, Dict[str, Any]]:
        """Run the tool."""
        try:
            result = self.requests_wrapper.get(_clean_url(url))
            return result

        except Exception as e:
            print(e)
            return 'The call has failed.'


class RequestsPostToolIInput(BaseModel):
    url: str = Field(..., description="the url to perform the request")
    data: str = Field(..., description="the data to POST to the url")


class RequestsPostTool(BaseRequestsTool, BaseTool):
    """Tool for making a POST request to an API endpoint."""

    name: str = "requests_post"
    description: str = """Use this when you want to POST to a website.
    Input should be a json string with two keys: "url" and "data".
    The value of "url" should be a string, and the value of "data" should be a dictionary of 
    key-value pairs you want to POST to the url.
    Be careful to always use double quotes for strings in the json string
    The output will be the text response of the POST request.
    """
    requests_wrapper = TextRequestsWrapper()
    args_schema: Type[BaseModel] = RequestsPostToolIInput

    def _run(
            self, url: str, data: str, run_manager: Optional[CallbackManagerForToolRun] = None
    ) -> Union[str, Dict[str, Any]]:
        """Run the tool."""
        try:
            data_dict = json.loads(data)
            result = self.requests_wrapper.post(_clean_url(url), data_dict)
            return result

        except Exception as e:
            print(e)
            return 'The data has not been sent to the server.'
