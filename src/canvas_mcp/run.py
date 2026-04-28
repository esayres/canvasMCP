# this is the main entry point for the application
from mcp.server.fastmcp import FastMCP
import requests

session = requests.Session() # create a session to reuse connections
tasks = [] # simple in-memory task list

# toy server with fastMCP

# Program Scope


# Features




# Create a server instance
mcp = FastMCP("CanvasMCP", log_level="DEBUG")

# Stateful Tools
@mcp.tool()
def add_task(task: str) -> str:
    """Add a new task (string) to the in-memory task list."""
    tasks.append(task)
    return "Task added."


# uv
def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()