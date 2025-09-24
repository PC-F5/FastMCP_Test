# FastMCP Demo Server 🚀

A simple MCP (Model Context Protocol) server built with FastMCP that provides basic mathematical operations.

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