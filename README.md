# FastMCP Demo Server 🚀

A simple MCP (Model Context Protocol) server built with FastMCP that provides basic mathematical operations.

## Documentation

For more information about FastMCP, visit: [https://gofastmcp.com/getting-started/welcome](https://gofastmcp.com/getting-started/welcome)

## Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Server
```bash
python server.py
```

The server will start on `http://127.0.0.1:3001/mcp` and display a banner with server information.

### 3. Connect to VS Code
1. Open the `.vscode/mcp.json` file
2. Click the **"Start Server"** button that appears above the `my-mcp-server-083ee277` block
3. The server will now be loaded and available in VS Code

## Available Tools

- **add**: Adds two integers together

## Available Resources

- **file://docs/llms.txt**: FastMCP documentation and links

## Testing with MCP Inspector

You can use the MCP Inspector to test and explore your server in a web browser:

```bash
npx @modelcontextprotocol/inspector
```

The MCP Inspector ([modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector)) is a visual testing tool that allows you to:
- Connect to your local MCP server
- Inspect available tools and resources
- Test tool execution with different parameters
- View resource contents
- Debug your MCP server implementation

Simply run the inspector command and navigate to the provided URL in your browser to start testing your server.

## Troubleshooting

- Make sure the server is running before trying to connect from VS Code
- The server must be running on port 3001 to match the configuration
- Check the VS Code output panel for any connection errors

## Server Configuration

The server configuration is defined in `.vscode/mcp.json`:
```json
{
    "servers": {
        "my-mcp-server-083ee277": {
            "type": "http",
            "url": "http://127.0.0.1:3001/mcp"
        }
    }
}
```