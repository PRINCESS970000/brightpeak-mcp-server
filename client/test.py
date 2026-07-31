import fastmcp.client

print(dir(fastmcp.client))
from fastmcp.client import Client

print(Client)
from fastmcp.client import Client
import inspect

print(inspect.signature(Client))