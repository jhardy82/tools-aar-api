"""
AAR System REST API - Sacred Geometry Framework
Phase 4.2: FastAPI Implementation with φ-Optimization

This module implements the core REST API for the AAR system, following
Sacred Geometry principles for optimal performance and structure.

Sacred Geometry Implementation:
- Circle: Complete request-response lifecycle
- Triangle: Three-tier security (authentication, authorization, validation)
- Spiral: Progressive API versioning and feature enhancement
- Golden Ratio: φ-based rate limiting and resource allocation
- Fractal: Self-similar endpoint patterns across all API routes
"""

import math
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, List, Optional

# Add modules path for AAR system integration first
modules_path = Path(__file__).parent.parent / "modules"
sys.path.insert(0, str(modules_path))

# Try to import external dependencies with fallback handling
try:
    import jwt
    import uvicorn
    from fastapi import Depends, FastAPI, HTTPException, WebSocket, status
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.middleware.trustedhost import TrustedHostMiddleware
    from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
    from passlib.context import CryptContext
    from pydantic import BaseModel, Field

    EXTERNAL_DEPS_AVAILABLE = True
except ImportError as import_error:
    print(f"⚠️ External dependencies not available: {import_error}")
    EXTERNAL_DEPS_AVAILABLE = False

    # Create mock classes for development
    class BaseModel:  # pylint: disable=too-few-public-methods,function-redefined
        """Mock BaseModel for development when Pydantic not available"""

        def __init__(self, **kwargs):  # pylint: disable=unused-argument
            pass

    def Field(*args, **kwargs):  # pylint: disable=unused-argument
        """Mock Field function for development when Pydantic not available"""
        return None


# Import API endpoints
try:
    from .endpoints import router

    ENDPOINTS_AVAILABLE = True
except ImportError as e:
    print(f"⚠️ Endpoints not available: {e}")
    ENDPOINTS_AVAILABLE = False
    router = None
# Import local modules with fallback handling
try:
    from modules.config.manager import ConfigurationManager
    from modules.plugins.manager import create_plugin_manager
    from modules.utils.safe_logging import get_safe_logger

    LOCAL_MODULES_AVAILABLE = True
except ImportError as import_error:
    print(f"⚠️ Local modules not available: {import_error}")
    LOCAL_MODULES_AVAILABLE = False

    # Create fallback classes
    class ConfigurationManager:
        def __init__(self):
            self._settings = {}

        def get_all_settings(self):
            return self._settings

        def set(self, key, value):
            self._settings[key] = value
            return True

    def create_plugin_manager():
        class MockPluginManager:
            def get_available_plugins(self):
                return []

            def discover_and_load_plugins(self):
                return {}

            def shutdown(self):
                pass

        return MockPluginManager()

    # Create basic logger fallback
    import logging

    def get_safe_logger(name):
        return logging.getLogger(name)


# Sacred Geometry constants
PHI = (1 + math.sqrt(5)) / 2
PHI_SQUARED = PHI * PHI  # φ² for advanced calculations
PHI_CUBED = PHI_SQUARED * PHI  # φ³ for priority calculations

# Initialize logger
logger = get_safe_logger(__name__)

# API Configuration with Sacred Geometry optimization
API_CONFIG = {
    "title": "AAR System API",
    "description": "After Action Review System API with Sacred Geometry Optimization",
    "version": "4.2.0",
    "phi_version": f"{PHI:.6f}",
    "contact": {
        "name": "Sacred Geometry Framework",
        "url": "https://github.com/sacred-geometry/aar-system",
    },
    "license_info": {
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
}

# JWT Configuration with φ-optimization
JWT_SECRET_KEY = (
    "sacred-geometry-phi-optimized-key-2025"  # In production, use environment variable
)
JWT_ALGORITHM = "HS256"
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = int(
    30 * PHI
)  # φ-optimized token lifetime: ~48.5 minutes

# Rate limiting with Golden Ratio intervals
RATE_LIMIT_REQUESTS = int(100 * PHI)  # ~162 requests
RATE_LIMIT_WINDOW = int(60 * PHI)  # ~97 seconds (φ-optimized window)

# Initialize FastAPI app with Sacred Geometry principles
app = FastAPI(**API_CONFIG)


# Application state to avoid global variables
class AppState:
    """Application state container to avoid global variables"""

    def __init__(self):
        self.plugin_manager = None
        self.config_manager = None
        self.startup_time = time.time()


app.state = AppState()

# Add CORS middleware with φ-optimized settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    max_age=int(600 * PHI),  # φ-optimized preflight cache: ~971 seconds
)

# Add trusted host middleware for security
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["*"],  # In production, specify actual hosts
)


# Include API endpoints
if ENDPOINTS_AVAILABLE and router:
    app.include_router(router)
    logger.info("API endpoints included")
else:
    logger.warning("API endpoints not available")

# Initialize core components (avoid global variables by using app.state)
# Initialized in startup_event
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
security = HTTPBearer()

# Rate limiting storage (in production, use Redis)
rate_limit_storage: Dict[str, List[float]] = {}


# Pydantic models for API requests/responses
class SystemStatusResponse(BaseModel):
    """System status response with Sacred Geometry metrics"""

    status: str = Field(..., description="System operational status")
    timestamp: float = Field(..., description="Current timestamp")
    sacred_geometry_score: float = Field(..., description="Overall φ-compliance score")
    phi_constant: float = Field(default=PHI, description="Golden Ratio constant")
    uptime_seconds: float = Field(..., description="System uptime in seconds")
    plugin_count: int = Field(..., description="Number of loaded plugins")
    active_connections: int = Field(..., description="Active WebSocket connections")


class PluginInfo(BaseModel):
    """Plugin information model"""

    name: str = Field(..., description="Plugin name")
    version: str = Field(..., description="Plugin version")
    description: str = Field(..., description="Plugin description")
    author: str = Field(..., description="Plugin author")
    sacred_geometry_score: float = Field(..., description="Plugin φ-compliance score")
    loaded: bool = Field(..., description="Plugin load status")
    performance_metrics: Dict[str, Any] = Field(
        default_factory=dict, description="Performance data"
    )


class PluginExecutionRequest(BaseModel):
    """Plugin execution request model"""

    plugin_name: str = Field(..., description="Name of plugin to execute")
    input_data: Optional[Dict[str, Any]] = Field(
        default=None, description="Input data for plugin"
    )
    parameters: Optional[Dict[str, Any]] = Field(
        default=None, description="Additional parameters"
    )
    timeout: Optional[float] = Field(
        default=None, description="Execution timeout (φ-optimized)"
    )


class PluginExecutionResponse(BaseModel):
    """Plugin execution response model"""

    success: bool = Field(..., description="Execution success status")
    result: Optional[Dict[str, Any]] = Field(
        default=None, description="Plugin execution result"
    )
    execution_time: float = Field(..., description="Execution time in seconds")
    sacred_geometry_score: float = Field(..., description="Result φ-compliance score")
    error_message: Optional[str] = Field(
        default=None, description="Error message if failed"
    )


class AuthToken(BaseModel):
    """Authentication token model"""

    access_token: str = Field(..., description="JWT access token")
    token_type: str = Field(default="bearer", description="Token type")
    expires_in: int = Field(..., description="Token expiration time in seconds")
    phi_optimized: bool = Field(default=True, description="Token uses φ-optimization")


class UserLogin(BaseModel):
    """User login request model"""

    username: str = Field(..., description="Username")
    password: str = Field(..., description="Password")


# WebSocket connection manager
class ConnectionManager:
    """WebSocket connection manager with Sacred Geometry optimization"""

    def __init__(self):
        self.active_connections: List[WebSocket] = []
        self.connection_count = 0
        self.phi_heartbeat_interval = 30 * PHI  # φ-optimized heartbeat: ~48.5 seconds

    async def connect(self, websocket: WebSocket):
        """Accept WebSocket connection"""
        await websocket.accept()
        self.active_connections.append(websocket)
        self.connection_count += 1
        logger.info("WebSocket connected. Total connections: %d", self.connection_count)

    def disconnect(self, websocket: WebSocket):
        """Remove WebSocket connection"""
        if websocket in self.active_connections:
            self.active_connections.remove(websocket)
            self.connection_count = max(0, self.connection_count - 1)
            logger.info(
                "WebSocket disconnected. Total connections: %d", self.connection_count
            )

    async def send_personal_message(
        self, message: Dict[str, Any], websocket: WebSocket
    ):
        """Send message to specific WebSocket"""
        try:
            await websocket.send_json(message)
        except (ConnectionResetError, ConnectionAbortedError) as e:
            logger.error("WebSocket connection error: %s", e)
            self.disconnect(websocket)
        except Exception as e:  # pylint: disable=broad-except
            # Broad exception needed for various WebSocket errors
            logger.error("Failed to send WebSocket message: %s", e)
            self.disconnect(websocket)

    async def broadcast(self, message: Dict[str, Any]):
        """Broadcast message to all connected WebSockets"""
        disconnected = []
        for connection in self.active_connections:
            try:
                await connection.send_json(message)
            except (ConnectionResetError, ConnectionAbortedError) as e:
                logger.error("WebSocket connection error during broadcast: %s", e)
                disconnected.append(connection)
            except Exception as e:  # pylint: disable=broad-except
                # Broad exception needed for various WebSocket errors
                logger.error("Failed to broadcast to WebSocket: %s", e)
                disconnected.append(connection)

        # Clean up disconnected WebSockets
        for connection in disconnected:
            self.disconnect(connection)


# Initialize WebSocket manager
manager = ConnectionManager()


# Authentication and security functions
def create_access_token(
    data: Dict[str, Any], expires_delta: Optional[timedelta] = None
) -> str:
    """Create JWT access token with φ-optimization"""
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire, "phi_optimized": True})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt


async def verify_token(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> Dict[str, Any]:
    """Verify JWT token with Sacred Geometry validation"""
    try:
        payload = jwt.decode(
            credentials.credentials, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM]
        )

        # Verify φ-optimization flag
        if not payload.get("phi_optimized", False):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token not φ-optimized",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return payload

    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expired",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    except jwt.JWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


async def check_rate_limit(client_ip: str) -> bool:
    """Check rate limit with φ-based intervals"""
    current_time = time.time()

    if client_ip not in rate_limit_storage:
        rate_limit_storage[client_ip] = []

    # Clean old requests (outside φ-optimized window)
    cutoff_time = current_time - RATE_LIMIT_WINDOW
    rate_limit_storage[client_ip] = [
        req_time for req_time in rate_limit_storage[client_ip] if req_time > cutoff_time
    ]

    # Check if within rate limit
    if len(rate_limit_storage[client_ip]) >= RATE_LIMIT_REQUESTS:
        return False

    # Add current request
    rate_limit_storage[client_ip].append(current_time)
    return True


# Startup and shutdown events
@app.on_event("startup")
async def startup_event():
    """Initialize system components on startup"""

    try:
        # Initialize configuration manager
        app.state.config_manager = ConfigurationManager()
        logger.info("Configuration manager initialized")

        # Initialize plugin manager
        app.state.plugin_manager = create_plugin_manager()
        logger.info("Plugin manager initialized")

        # Discover and load plugins
        if hasattr(app.state.plugin_manager, "discover_and_load_plugins"):
            plugin_results = app.state.plugin_manager.discover_and_load_plugins()
            logger.info(
                "Plugins loaded: %d/%d",
                sum(plugin_results.values()),
                len(plugin_results),
            )

        logger.info("🌟 AAR API System started with Sacred Geometry optimization")

    except Exception as e:
        logger.error("Failed to initialize system components: %s", e)
        raise


@app.on_event("shutdown")
async def shutdown_event():
    """Cleanup on shutdown"""

    try:
        if app.state.plugin_manager and hasattr(app.state.plugin_manager, "shutdown"):
            app.state.plugin_manager.shutdown()
            logger.info("Plugin manager shutdown complete")

        logger.info("🔺 AAR API System shutdown complete")

    except Exception as e:  # pylint: disable=broad-except
        # Broad exception needed during shutdown to prevent application hanging
        logger.error("Error during shutdown: %s", e)


# API Routes
@app.get("/", response_model=Dict[str, Any])
async def root():
    """Root endpoint with Sacred Geometry information"""
    return {
        "message": "AAR System API with Sacred Geometry Optimization",
        "version": API_CONFIG["version"],
        "phi_constant": PHI,
        "sacred_geometry_principles": [
            "Circle: Complete request-response lifecycle",
            "Triangle: Three-tier security architecture",
            "Spiral: Progressive API versioning",
            "Golden Ratio: φ-optimized rate limiting",
            "Fractal: Self-similar endpoint patterns",
        ],
        "api_documentation": "/docs",
        "websocket_endpoint": "/ws",
        "timestamp": time.time(),
    }


@app.get("/api/v1/system/status", response_model=SystemStatusResponse)
async def get_system_status():
    """Get comprehensive system status with Sacred Geometry metrics"""
    try:
        # Calculate Sacred Geometry score based on system health
        plugin_count = (
            len(app.state.plugin_manager.get_available_plugins())
            if app.state.plugin_manager
            else 0
        )
        active_connections = manager.connection_count

        # φ-based scoring algorithm
        base_score = 0.618  # Base φ ratio
        plugin_score = min(plugin_count * 0.1, 0.5)  # Plugin contribution
        connection_score = min(
            active_connections * 0.05, 0.3
        )  # Connection contribution
        sacred_geometry_score = min(
            (base_score + plugin_score + connection_score) * PHI, PHI
        )

        return SystemStatusResponse(
            status="operational",
            timestamp=time.time(),
            sacred_geometry_score=sacred_geometry_score,
            uptime_seconds=time.time() - app.state.startup_time,
            plugin_count=plugin_count,
            active_connections=active_connections,
        )

    except Exception as e:
        logger.error("Failed to get system status: %s", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to retrieve system status",
        ) from e


if __name__ == "__main__":
    # Development server with φ-optimized settings
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=int(8000 * PHI / PHI),  # Port 8000 (φ-neutral)
        reload=True,
        workers=1,
        log_level="info",
    )
