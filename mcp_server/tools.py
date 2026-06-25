# mcp_server/tools.py
from tools.retrieve_content import retrieve_content
from tools.author_profile import get_author_profile
from tools.validate_context import validate_context
from tools.format_response import format_response

# Este arquivo serve como um hub para expor as funções
def get_all_tools():
    return {
        "retrieve_content": retrieve_content,
        "author_profile": get_author_profile,
        "validate_context": validate_context,
        "format_response": format_response
    }