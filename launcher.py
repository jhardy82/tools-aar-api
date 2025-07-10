"""
AAR System API Launcher
Phase 4.2: Complete API Server with Sacred Geometry Optimization

This script launches the complete AAR API server with all endpoints,
WebSocket support, and Sacred Geometry optimization.
"""

import sys
import time
from pathlib import Path

# Add modules path
modules_path = Path(__file__).parent.parent / "modules"
sys.path.insert(0, str(modules_path))

try:
    import uvicorn
    from fastapi.responses import HTMLResponse

    # Import our API components
    from main import PHI, app

    # Try to import startup_time, but handle if not available
    try:
        from main import manager  # pylint: disable=unused-import
    except ImportError:
        startup_time = time.time()
        manager = None

    # Try to import endpoints (may fail if dependencies missing)
    try:
        from endpoints import router as endpoints_router
        from websockets import websocket_router

        # Add routers to the main app
        app.include_router(endpoints_router)
        app.include_router(websocket_router)

        FULL_API_AVAILABLE = True
    except ImportError as e:
        print(f"⚠️ Some API features unavailable (missing dependencies): {e}")
        FULL_API_AVAILABLE = False

except ImportError:
    print("⚠️ FastAPI not available. Installing required packages...")
    FULL_API_AVAILABLE = False
    app = None


def create_simple_html_dashboard():
    """Create a simple HTML dashboard for the API"""
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AAR System API - Sacred Geometry Dashboard</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        .header {{
            text-align: center;
            margin-bottom: 40px;
        }}
        .phi-symbol {{
            font-size: 3em;
            color: #FFD700;
            margin: 20px 0;
        }}
        .api-card {{
            background: rgba(255, 255, 255, 0.1);
            border-radius: 15px;
            padding: 30px;
            margin: 20px 0;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        .endpoint-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        .endpoint {{
            background: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid #FFD700;
        }}
        .method {{
            display: inline-block;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
            margin-right: 10px;
        }}
        .get {{ background: #4CAF50; }}
        .post {{ background: #2196F3; }}
        .put {{ background: #FF9800; }}
        .websocket {{ background: #9C27B0; }}
        .phi-metric {{
            background: linear-gradient(45deg, #FFD700, #FFA500);
            color: #333;
            padding: 15px;
            border-radius: 10px;
            margin: 10px 0;
            text-align: center;
            font-weight: bold;
        }}
        .status-indicator {{
            display: inline-block;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            margin-right: 8px;
        }}
        .online {{ background: #4CAF50; }}
        .offline {{ background: #f44336; }}
        .footer {{
            text-align: center;
            margin-top: 40px;
            opacity: 0.8;
        }}
        .websocket-demo {{
            background: rgba(156, 39, 176, 0.1);
            border: 2px solid #9C27B0;
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
        }}
        #wsStatus {{
            font-weight: bold;
            margin: 10px 0;
        }}
        #wsMessages {{
            background: rgba(0, 0, 0, 0.3);
            border-radius: 5px;
            padding: 15px;
            height: 200px;
            overflow-y: auto;
            font-family: monospace;
            font-size: 12px;
            margin: 10px 0;
        }}
        button {{
            background: linear-gradient(45deg, #FFD700, #FFA500);
            color: #333;
            border: none;
            padding: 10px 20px;
            border-radius: 25px;
            cursor: pointer;
            font-weight: bold;
            margin: 5px;
            transition: transform 0.2s;
        }}
        button:hover {{
            transform: scale(1.05);
        }}
        .phi-animation {{
            animation: phi-pulse 3s infinite;
        }}
        @keyframes phi-pulse {{
            0%, 100% {{ opacity: 1; transform: scale(1); }}
            50% {{ opacity: 0.7; transform: scale(1.05); }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌀 AAR System API</h1>
            <div class="phi-symbol phi-animation">φ</div>
            <h2>Sacred Geometry Framework</h2>
            <p>Phase 4.2: Complete REST API with φ-Optimization</p>
        </div>

        <div class="api-card">
            <h3><span class="status-indicator {"online" if FULL_API_AVAILABLE else "offline"}"></span>
                API Status: {"Fully Operational" if FULL_API_AVAILABLE else "Limited (Missing Dependencies)"}</h3>

            <div class="phi-metric">
                Golden Ratio (φ): {PHI:.6f}
            </div>

            <div class="phi-metric">
                Server Uptime: <span id="uptime">Calculating...</span>
            </div>
        </div>

        <div class="api-card">
            <h3>🔗 API Endpoints</h3>
            <div class="endpoint-list">
                <div class="endpoint">
                    <div><span class="method get">GET</span><code>/</code></div>
                    <p>Root endpoint with Sacred Geometry info</p>
                </div>
                <div class="endpoint">
                    <div><span class="method get">GET</span><code>/api/v1/system/status</code></div>
                    <p>System status with φ-metrics</p>
                </div>
                <div class="endpoint">
                    <div><span class="method post">POST</span><code>/api/v1/auth/login</code></div>
                    <p>Authentication with φ-optimized tokens</p>
                </div>
                <div class="endpoint">
                    <div><span class="method get">GET</span><code>/api/v1/plugins</code></div>
                    <p>List all available plugins</p>
                </div>
                <div class="endpoint">
                    <div><span class="method post">POST</span><code>/api/v1/plugins/{{name}}/execute</code></div>
                    <p>Execute plugin with Sacred Geometry scoring</p>
                </div>
                <div class="endpoint">
                    <div><span class="method post">POST</span><code>/api/v1/analysis/trigger</code></div>
                    <p>Trigger comprehensive system analysis</p>
                </div>
                <div class="endpoint">
                    <div><span class="method get">GET</span><code>/api/v1/config</code></div>
                    <p>Get system configuration</p>
                </div>
                <div class="endpoint">
                    <div><span class="method websocket">WS</span><code>/ws</code></div>
                    <p>Real-time WebSocket communication</p>
                </div>
            </div>
        </div>

        <div class="api-card">
            <h3>📊 Interactive API Documentation</h3>
            <p>Explore the complete API with interactive Swagger documentation:</p>
            <button onclick="window.open('/docs', '_blank')">🚀 Open API Docs</button>
            <button onclick="window.open('/redoc', '_blank')">📖 ReDoc Documentation</button>
        </div>

        <div class="websocket-demo">
            <h3>🔗 WebSocket Demo</h3>
            <div id="wsStatus">Status: Disconnected</div>
            <button id="connectBtn" onclick="connectWebSocket()">Connect WebSocket</button>
            <button id="pingBtn" onclick="sendPing()" disabled>Send Ping</button>
            <button id="statusBtn" onclick="getStatus()" disabled>Get Status</button>
            <div id="wsMessages"></div>
        </div>

        <div class="footer">
            <p>🔺 Sacred Geometry Principles: Circle • Triangle • Spiral • Golden Ratio • Fractal</p>
            <p>Built with φ-optimization for mathematical harmony and peak performance</p>
            <p>© 2025 Sacred Geometry Framework - Phase 4.2</p>
        </div>
    </div>

    <script>
        let ws = null;
        let startTime = {int(time.time() * 1000)};

        function updateUptime() {{
            const now = Date.now();
            const uptimeMs = now - startTime;
            const seconds = Math.floor(uptimeMs / 1000);
            const minutes = Math.floor(seconds / 60);
            const hours = Math.floor(minutes / 60);

            let uptimeStr = '';
            if (hours > 0) uptimeStr += hours + 'h ';
            if (minutes % 60 > 0) uptimeStr += (minutes % 60) + 'm ';
            uptimeStr += (seconds % 60) + 's';

            document.getElementById('uptime').textContent = uptimeStr;
        }}

        function connectWebSocket() {{
            const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
            const wsUrl = `${{protocol}}//${{window.location.host}}/ws?client_id=dashboard_${{Date.now()}}`;

            ws = new WebSocket(wsUrl);

            ws.onopen = function() {{
                document.getElementById('wsStatus').textContent = 'Status: Connected';
                document.getElementById('connectBtn').disabled = true;
                document.getElementById('pingBtn').disabled = false;
                document.getElementById('statusBtn').disabled = false;
                addMessage('✅ Connected to WebSocket');
            }};

            ws.onmessage = function(event) {{
                const data = JSON.parse(event.data);
                addMessage(`📨 ${{data.type}}: ${{JSON.stringify(data, null, 2)}}`);
            }};

            ws.onclose = function() {{
                document.getElementById('wsStatus').textContent = 'Status: Disconnected';
                document.getElementById('connectBtn').disabled = false;
                document.getElementById('pingBtn').disabled = true;
                document.getElementById('statusBtn').disabled = true;
                addMessage('❌ WebSocket disconnected');
            }};

            ws.onerror = function(error) {{
                addMessage(`❌ WebSocket error: ${{error}}`);
            }};
        }}

        function sendPing() {{
            if (ws && ws.readyState === WebSocket.OPEN) {{
                ws.send(JSON.stringify({{
                    type: 'ping',
                    timestamp: Date.now()
                }}));
                addMessage('📤 Sent ping');
            }}
        }}

        function getStatus() {{
            if (ws && ws.readyState === WebSocket.OPEN) {{
                ws.send(JSON.stringify({{
                    type: 'get_status'
                }}));
                addMessage('📤 Requested status');
            }}
        }}

        function addMessage(message) {{
            const messagesDiv = document.getElementById('wsMessages');
            const timestamp = new Date().toLocaleTimeString();
            messagesDiv.innerHTML += `[${{timestamp}}] ${{message}}\\n`;
            messagesDiv.scrollTop = messagesDiv.scrollHeight;
        }}

        // Update uptime every second
        setInterval(updateUptime, 1000);
        updateUptime();
    </script>
</body>
</html>
"""
    return html_content


def install_dependencies():
    """Install required dependencies for the API server"""
    import subprocess

    required_packages = [
        "fastapi>=0.104.0",
        "uvicorn[standard]>=0.24.0",
        "python-jose[cryptography]>=3.3.0",
        "passlib[bcrypt]>=1.7.4",
        "python-multipart>=0.0.6",
    ]

    print("📦 Installing required packages for AAR API...")
    for package in required_packages:
        try:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install {package}: {e}")
            return False

    print("✅ All packages installed successfully!")
    return True


def create_dashboard_route():
    """Create dashboard route if app is available"""
    if app and FULL_API_AVAILABLE:

        @app.get("/dashboard", response_class=HTMLResponse)
        async def dashboard():
            """Interactive dashboard for the AAR API"""
            return HTMLResponse(content=create_simple_html_dashboard())

    return app


def main():
    """Launch the AAR API server with Sacred Geometry optimization"""

    print("🌀 AAR System API Server")
    print("=" * 50)
    print(f"📐 Golden Ratio (φ): {PHI:.6f}")
    print("🔺 Sacred Geometry Framework: Phase 4.2")
    print()

    if not FULL_API_AVAILABLE:
        print("⚠️ API dependencies missing. Would you like to install them? (y/n)")
        response = input().lower().strip()

        if response in ["y", "yes"]:
            if install_dependencies():
                print("🔄 Please restart the server to use all features.")
                return
            else:
                print(
                    "❌ Failed to install dependencies. Running with limited features."
                )
        else:
            print("⚡ Running with basic features only.")

    print()
    print("🚀 Starting API server...")
    print("📊 Dashboard: http://localhost:8000/dashboard")
    print("📖 API Docs: http://localhost:8000/docs")
    print("🔗 WebSocket: ws://localhost:8000/ws")
    print()
    print("🔺 Sacred Geometry Optimization Active:")
    print(f"   • Rate Limiting: {int(100 * PHI)} requests per {int(60 * PHI)} seconds")
    print(f"   • Token Expiry: {int(30 * PHI)} minutes")
    print(f"   • WebSocket Heartbeat: {30 * PHI:.1f} seconds")
    print(f"   • Max Connections: {int(100 * PHI)}")
    print()

    try:
        # Run the server with φ-optimized settings
        uvicorn.run(
            "launcher:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            workers=1,
            log_level="info",
            access_log=True,
        )
    except ImportError:
        print("❌ FastAPI/Uvicorn not available. Please install required packages:")
        print(
            "   pip install fastapi uvicorn[standard] python-jose[cryptography] passlib[bcrypt]"
        )
        sys.exit(1)
    except KeyboardInterrupt:
        print("\\n🔺 Server shutdown requested")
        print("✅ AAR API Server stopped gracefully")
    except Exception as e:  # pylint: disable=broad-except
        # Broad exception needed here for graceful server shutdown
        print(f"❌ Server error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
