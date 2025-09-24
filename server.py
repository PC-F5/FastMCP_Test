from fastmcp import FastMCP
import os

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("file://docs/llms.txt")
def llms_documentation():
    """FastMCP documentation and links"""
    try:
        with open(os.path.join("docs", "llms.txt"), "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Documentation file not found."
    except Exception as e:
        return f"Error reading documentation: {str(e)}"

if __name__ == "__main__":
    mcp.run(port=3001, transport="http")