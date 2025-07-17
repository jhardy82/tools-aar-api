#!/usr/bin/env python3
"""
AAR System API Launcher - Fixed Version
Phase 4.2: Complete API Server with Sacred Geometry Optimization

This script launches the complete AAR API server with proper error handling
and dependency management.
"""

import math
import subprocess
import sys
from pathlib import Path

# Add modules path
modules_path = Path(__file__).parent.parent / "modules"
sys.path.insert(0, str(modules_path))

# Sacred Geometry constants
PHI = (1 + math.sqrt(5)) / 2


def install_dependencies():
    """Install required dependencies"""
    required_packages = [
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
    ]

    print("📦 Installing required packages...")
    for package in required_packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False

    print("✅ All packages installed successfully!")
    return True


def check_dependencies():
    """Check if required dependencies are available"""
    try:
        import fastapi
        import jwt
        import passlib
        import uvicorn

        return True
    except ImportError as e:
        print(f"⚠️ Missing dependencies: {e}")
        return False


def create_simple_html_dashboard():
    """Create a simple HTML dashboard for the API"""
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AAR System API Dashboard - Sacred Geometry Framework</title>
    <style>
        body {{
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 20px;
            color: white;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px rgba(31, 38, 135, 0.37);
        }}
        h1 {{
            text-align: center;
            color: #FFD700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
            margin-bottom: 30px;
        }}
        .phi-display {{
            text-align: center;
            font-size: 1.5em;
            color: #FFD700;
            margin: 20px 0;
        }}
        .api-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        .api-card {{
            background: rgba(255, 255, 255, 0.15);
            border-radius: 10px;
            padding: 20px;
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .api-card h3 {{
            color: #FFD700;
            margin-top: 0;
        }}
        .endpoint {{
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            font-family: monospace;
        }}
        .status {{
            text-align: center;
            padding: 20px;
            background: rgba(0, 255, 0, 0.2);
            border-radius: 10px;
            margin: 20px 0;
        }}
        .websocket-demo {{
            background: rgba(255, 255, 255, 0.1);
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }}
        #wsMessages {{
            height: 200px;
            overflow-y: auto;
            background: rgba(0, 0, 0, 0.3);
            padding: 10px;
            border-radius: 5px;
            font-family: monospace;
            font-size: 12px;
        }}
        button {{
            background: linear-gradient(45deg, #FFD700, #FFA500);
            color: black;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: bold;
            margin: 5px;
        }}
        button:hover {{
            transform: scale(1.05);
            transition: transform 0.2s;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🔺 AAR System API Dashboard</h1>
        <div class="phi-display">
            Sacred Geometry Framework - φ = {PHI:.6f}
        </div>

        <div class="status">
            <h2>🌟 System Status: Operational</h2>
            <p>API Server running with Sacred Geometry optimization</p>
            <p>Current Time: <span id="currentTime"></span></p>
        </div>

        <div class="api-grid">
            <div class="api-card">
                <h3>📊 System Endpoints</h3>
                <div class="endpoint">GET /api/v1/system/status</div>
                <div class="endpoint">GET /health</div>
                <div class="endpoint">GET /docs</div>
                <div class="endpoint">GET /redoc</div>
            </div>

            <div class="api-card">
                <h3>🔐 Authentication</h3>
                <div class="endpoint">POST /auth/login</div>
                <div class="endpoint">POST /auth/refresh</div>
                <div class="endpoint">GET /auth/me</div>
                <p><small>Default credentials: admin / sacred_geometry_2025</small></p>
            </div>

            <div class="api-card">
                <h3>🔌 Plugin Management</h3>
                <div class="endpoint">GET /plugins/</div>
                <div class="endpoint">POST /plugins/execute</div>
                <div class="endpoint">GET /plugins/{{name}}/status</div>
            </div>

            <div class="api-card">
                <h3>📈 Analysis</h3>
                <div class="endpoint">GET /analysis/system-status</div>
                <div class="endpoint">POST /analysis/sacred-geometry</div>
                <div class="endpoint">GET /analysis/workspace-intelligence</div>
            </div>
        </div>

        <div class="websocket-demo">
            <h3>📡 WebSocket Real-time Demo</h3>
            <div>
                <button onclick="connectWebSocket()">Connect WebSocket</button>
                <button onclick="disconnectWebSocket()">Disconnect</button>
                <button onclick="sendMessage()">Send Test Message</button>
            </div>
            <div id="wsMessages"></div>
        </div>

        <div style="text-align: center; margin-top: 30px;">
            <button onclick="window.open('/docs', '_blank')">📖 API Documentation</button>
            <button onclick="testAPI()">🧪 Test API</button>
            <button onclick="refreshDashboard()">🔄 Refresh</button>
        </div>
    </div>

    <script>
        let ws = null;

        function updateTime() {{
            document.getElementById('currentTime').textContent = new Date().toLocaleString();
        }}

        function connectWebSocket() {{
            const wsUrl = `ws://${{window.location.host}}/ws/realtime`;
            ws = new WebSocket(wsUrl);

            ws.onopen = function(event) {{
                addMessage('✅ WebSocket connected');
            }};

            ws.onmessage = function(event) {{
                const data = JSON.parse(event.data);
                addMessage(`📨 Received: ${{JSON.stringify(data, null, 2)}}`);
            }};

            ws.onclose = function(event) {{
                addMessage('❌ WebSocket disconnected');
            }};

            ws.onerror = function(error) {{
                addMessage(`❌ WebSocket error: ${{error}}`);
            }};
        }}

        function disconnectWebSocket() {{
            if (ws) {{
                ws.close();
                ws = null;
            }}
        }}

        function sendMessage() {{
            if (ws && ws.readyState === WebSocket.OPEN) {{
                const message = {{
                    type: 'test',
                    phi: {PHI},
                    timestamp: Date.now()
                }};
                ws.send(JSON.stringify(message));
                addMessage(`📤 Sent: ${{JSON.stringify(message)}}`);
            }} else {{
                addMessage('❌ WebSocket not connected');
            }}
        }}

        function addMessage(message) {{
            const messagesDiv = document.getElementById('wsMessages');
            const timestamp = new Date().toLocaleTimeString();
            messagesDiv.innerHTML += `${{timestamp}}: ${{message}}\\n`;
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }}

        function testAPI() {{
            fetch('/api/v1/system/status')
                .then(response => response.json())
                .then(data => {{
                    addMessage(`🧪 API Test Result: ${{JSON.stringify(data, null, 2)}}`);
                }})
                .catch(error => {{
                    addMessage(`❌ API Test Error: ${{error}}`);
                }});
        }}

        function refreshDashboard() {{
            location.reload();
        }}

        // Update time every second
        setInterval(updateTime, 1000);
        updateTime();
    </script>
</body>
</html>
"""
    return html_content


def start_api_server():
    """Start the API server"""
    try:
        # Check dependencies first
        if not check_dependencies():
            print("Missing dependencies. Attempting to install...")
            if not install_dependencies():
                return False

        # Import API components after ensuring dependencies
        import uvicorn
        from main import app

        # Try to add routes if endpoints are available
        try:
            from endpoints import router as endpoints_router
            from websockets import websocket_router

            app.include_router(endpoints_router)
            app.include_router(websocket_router)
            print("✅ All API routes loaded successfully")
        except ImportError as e:
            print(f"⚠️ Some API features unavailable: {e}")

        # Add dashboard route
        try:
            from fastapi.responses import HTMLResponse

            @app.get("/dashboard", response_class=HTMLResponse)
            async def dashboard():
                """Interactive dashboard for the AAR API"""
                return HTMLResponse(content=create_simple_html_dashboard())

            print("✅ Dashboard route added")
        except Exception as e:
            print(f"⚠️ Dashboard route failed: {e}")

        print("🚀 Starting AAR API Server...")
        print("Sacred Geometry Framework - Phase 4.2")
        print("=" * 50)
        print("📊 Dashboard: http://localhost:8000/dashboard")
        print("📖 API Docs: http://localhost:8000/docs")
        print("🔗 WebSocket: ws://localhost:8000/ws")
        print("=" * 50)

        # Start the server
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=8000,
            log_level="info",
            reload=False,  # Disable reload to prevent import issues
        )

        return True

    except Exception as e:
        print(f"❌ Failed to start API server: {e}")
        return False


def main():
    """Main launcher function"""
    print("🔺 AAR System API Launcher")
    print("Sacred Geometry Framework - Phase 4.2")
    print("=" * 50)

    if "--install-deps" in sys.argv:
        success = install_dependencies()
        return 0 if success else 1

    if "--test-mode" in sys.argv:
        print("🧪 Test mode: checking components...")
        if check_dependencies():
            print("✅ All dependencies available")
            return 0
        else:
            print("❌ Missing dependencies")
            return 1

    # Start the API server
    success = start_api_server()
    return 0 if success else 1


if __name__ == "__main__":
    exit(main())
