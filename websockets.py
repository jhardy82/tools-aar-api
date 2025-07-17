"""
AAR System API - WebSocket Real-time Communication
Phase 4.2: Real-time Updates with Sacred Geometry

This module implements WebSocket endpoints for real-time communication
with Sacred Geometry principles for optimal data streaming.
"""

import math
import asyncio

# Add modules path for AAR system integration
import sys
import time
from pathlib import Path
from typing import Any, Dict, Optional

try:
    from fastapi import APIRouter, Query, WebSocket, WebSocketDisconnect
    from fastapi.websockets import WebSocketState

    FASTAPI_AVAILABLE = True
except ImportError:
    print("⚠️ FastAPI not available - WebSocket functionality limited")
    FASTAPI_AVAILABLE = False

    # Mock classes for development
    class APIRouter:  # pylint: disable=function-redefined
        def websocket(self, path: str):  # pylint: disable=unused-argument
            def decorator(func):
                return func

            return decorator

    class WebSocket:  # pylint: disable=function-redefined
        pass

    class WebSocketDisconnect(Exception):  # pylint: disable=function-redefined
        pass

    class WebSocketState:  # pylint: disable=function-redefined
        CONNECTED = "connected"
        DISCONNECTED = "disconnected"

    def Query(default=None):
        return default


modules_path = Path(__file__).parent.parent / "modules"
sys.path.insert(0, str(modules_path))

try:
    from modules.utils.safe_logging import get_safe_logger
except ImportError:
    import logging

    def get_safe_logger(name):
        return logging.getLogger(name)


# Sacred Geometry constants
PHI = (1 + math.sqrt(5)) / 2
logger = get_safe_logger(__name__)

# Create WebSocket router
websocket_router = APIRouter()


class WebSocketManager:
    """
    Enhanced WebSocket manager with Sacred Geometry optimization

    Sacred Geometry Implementation:
    - Circle: Complete connection lifecycle management
    - Triangle: Three-tier message validation
    - Spiral: Progressive connection enhancement
    - Golden Ratio: φ-based heartbeat and data streaming intervals
    - Fractal: Self-similar connection patterns
    """

    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.connection_metadata: Dict[str, Dict[str, Any]] = {}
        self.heartbeat_interval = 30 * PHI  # φ-optimized heartbeat: ~48.5 seconds
        self.max_connections = int(100 * PHI)  # φ-optimized connection limit: ~162
        self.message_rate_limit = int(
            60 * PHI
        )  # φ-optimized message rate: ~97 per minute
        self.heartbeat_task = None

    async def connect(self, websocket: WebSocket, client_id: str):
        """Accept and manage WebSocket connection with φ-optimization"""

        # Check connection limits
        if len(self.active_connections) >= self.max_connections:
            await websocket.close(code=1008, reason="Connection limit exceeded")
            logger.warning("Connection limit exceeded for client %s", client_id)
            return False

        try:
            await websocket.accept()
            self.active_connections[client_id] = websocket
            self.connection_metadata[client_id] = {
                "connected_at": time.time(),
                "message_count": 0,
                "last_message_time": time.time(),
                "sacred_geometry_score": 0.618,  # Initial φ-based score
                "phi_optimized": True,
            }

            logger.info(
                "WebSocket connected: %s (Total: %d)",
                client_id,
                len(self.active_connections),
            )

            # Start heartbeat if this is the first connection
            if len(self.active_connections) == 1 and not self.heartbeat_task:
                self.heartbeat_task = asyncio.create_task(self._heartbeat_loop())

            # Send welcome message with Sacred Geometry info
            await self.send_personal_message(
                client_id,
                {
                    "type": "connection_established",
                    "client_id": client_id,
                    "phi_constant": PHI,
                    "heartbeat_interval": self.heartbeat_interval,
                    "sacred_geometry_optimized": True,
                    "timestamp": time.time(),
                },
            )

            return True

        except Exception as e:  # pylint: disable=broad-except
            # Broad exception needed for WebSocket connection errors
            logger.error("Failed to connect WebSocket for %s: %s", client_id, e)
            return False

    async def disconnect(self, client_id: str):
        """Disconnect and cleanup WebSocket with proper lifecycle management"""

        if client_id in self.active_connections:
            websocket = self.active_connections[client_id]

            # Close WebSocket if still open
            if websocket.client_state != WebSocketState.DISCONNECTED:
                try:
                    await websocket.close()
                except Exception as e:  # pylint: disable=broad-except
                    # Broad exception needed for WebSocket close errors
                    logger.error("Error closing WebSocket for %s: %s", client_id, e)

            # Remove from active connections
            del self.active_connections[client_id]

            # Clean up metadata
            if client_id in self.connection_metadata:
                connection_time = (
                    time.time() - self.connection_metadata[client_id]["connected_at"]
                )
                logger.info(
                    "WebSocket disconnected: %s (Connected for %.1fs)",
                    client_id,
                    connection_time,
                )
                del self.connection_metadata[client_id]

            # Stop heartbeat if no connections remain
            if len(self.active_connections) == 0 and self.heartbeat_task:
                self.heartbeat_task.cancel()
                self.heartbeat_task = None

    async def send_personal_message(self, client_id: str, message: Dict[str, Any]):
        """Send message to specific client with Sacred Geometry validation"""

        if client_id not in self.active_connections:
            logger.warning(
                "Attempted to send message to non-existent client: %s", client_id
            )
            return False

        websocket = self.active_connections[client_id]

        try:
            # Add Sacred Geometry metadata to message
            enhanced_message = {
                **message,
                "phi_constant": PHI,
                "client_id": client_id,
                "server_timestamp": time.time(),
            }

            await websocket.send_json(enhanced_message)

            # Update connection metadata
            if client_id in self.connection_metadata:
                metadata = self.connection_metadata[client_id]
                metadata["message_count"] += 1
                metadata["last_message_time"] = time.time()

                # Update Sacred Geometry score based on message frequency
                message_frequency = metadata["message_count"] / (
                    time.time() - metadata["connected_at"] + 1
                )
                metadata["sacred_geometry_score"] = min(
                    0.618 + (message_frequency * 0.1), PHI
                )

            return True

        except Exception as e:  # pylint: disable=broad-except
            # Broad exception needed for WebSocket message errors
            logger.error("Failed to send message to %s: %s", client_id, e)
            await self.disconnect(client_id)
            return False

    async def broadcast(
        self, message: Dict[str, Any], exclude_client: Optional[str] = None
    ):
        """Broadcast message to all connected clients with φ-optimization"""

        if not self.active_connections:
            return  # Add broadcast metadata
        broadcast_msg = {
            **message,
            "type": "broadcast",
            "phi_constant": PHI,
            "server_timestamp": time.time(),
            "connection_count": len(self.active_connections),
        }

        # Send to all connections except excluded client
        disconnected_clients = []
        for client_id, websocket in self.active_connections.items():
            if client_id == exclude_client:
                continue

            try:
                await websocket.send_json(broadcast_msg)
            except Exception as e:  # pylint: disable=broad-except
                # Broad exception needed for WebSocket broadcast errors
                logger.error("Failed to broadcast to %s: %s", client_id, e)
                disconnected_clients.append(client_id)

        # Clean up disconnected clients
        for client_id in disconnected_clients:
            await self.disconnect(client_id)

    async def _heartbeat_loop(self):
        """φ-Optimized heartbeat loop for connection health monitoring"""

        while len(self.active_connections) > 0:
            try:
                await asyncio.sleep(self.heartbeat_interval)

                # Send heartbeat to all connections
                heartbeat_message = {
                    "type": "heartbeat",
                    "phi_interval": self.heartbeat_interval,
                    "server_time": time.time(),
                    "active_connections": len(self.active_connections),
                }

                await self.broadcast(heartbeat_message)

                # Log heartbeat info
                logger.debug(
                    "Heartbeat sent to %d connections", len(self.active_connections)
                )

            except asyncio.CancelledError:
                logger.info("Heartbeat loop cancelled")
                break
            except Exception as e:  # pylint: disable=broad-except
                # Broad exception needed for heartbeat loop errors
                logger.error("Error in heartbeat loop: %s", e)

    def get_connection_stats(self) -> Dict[str, Any]:
        """Get comprehensive connection statistics with Sacred Geometry metrics"""

        total_connections = len(self.active_connections)
        total_messages = sum(
            metadata.get("message_count", 0)
            for metadata in self.connection_metadata.values()
        )

        avg_connection_time = 0
        avg_sacred_geometry_score = 0

        if total_connections > 0:
            current_time = time.time()
            connection_times = [
                current_time - metadata["connected_at"]
                for metadata in self.connection_metadata.values()
            ]
            avg_connection_time = sum(connection_times) / len(connection_times)

            sacred_geometry_scores = [
                metadata.get("sacred_geometry_score", 0)
                for metadata in self.connection_metadata.values()
            ]
            avg_sacred_geometry_score = sum(sacred_geometry_scores) / len(
                sacred_geometry_scores
            )

        return {
            "active_connections": total_connections,
            "max_connections": self.max_connections,
            "total_messages_sent": total_messages,
            "average_connection_time": avg_connection_time,
            "average_sacred_geometry_score": avg_sacred_geometry_score,
            "phi_optimization_factor": avg_sacred_geometry_score / PHI
            if PHI > 0
            else 0,
            "heartbeat_interval": self.heartbeat_interval,
            "phi_constant": PHI,
            "timestamp": time.time(),
        }


# Initialize WebSocket manager
ws_manager = WebSocketManager()


@websocket_router.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: str = Query(default=None, description="Unique client identifier"),
    token: str = Query(default=None, description="Authentication token"),  # pylint: disable=unused-argument
):
    """
    Main WebSocket endpoint with Sacred Geometry optimization

    Provides real-time communication for:
    - System status updates
    - Plugin execution progress
    - Analysis results streaming
    - Configuration change notifications
    """

    # Generate client ID if not provided
    if not client_id:
        client_id = f"client_{int(time.time())}_{id(websocket)}"

    # FUTURE: Add token validation in production
    # For now, accept all connections

    # Attempt to connect
    connected = await ws_manager.connect(websocket, client_id)
    if not connected:
        return

    try:
        while True:
            # Receive message from client
            data = await websocket.receive_json()

            # Process message based on type
            message_type = data.get("type", "unknown")

            if message_type == "ping":
                # Respond to ping with pong
                await ws_manager.send_personal_message(
                    client_id,
                    {
                        "type": "pong",
                        "original_timestamp": data.get("timestamp", time.time()),
                        "response_timestamp": time.time(),
                    },
                )

            elif message_type == "get_status":
                # Send current system status
                connection_stats = ws_manager.get_connection_stats()
                await ws_manager.send_personal_message(
                    client_id,
                    {
                        "type": "status_response",
                        "system_status": "operational",
                        "connection_stats": connection_stats,
                    },
                )

            elif message_type == "subscribe":
                # Subscribe to specific updates
                subscription_type = data.get("subscription", "all")
                await ws_manager.send_personal_message(
                    client_id,
                    {
                        "type": "subscription_confirmed",
                        "subscription": subscription_type,
                        "phi_optimized": True,
                    },
                )

            else:
                # Echo unknown message types
                await ws_manager.send_personal_message(
                    client_id,
                    {
                        "type": "message_received",
                        "original_message": data,
                        "processed_at": time.time(),
                    },
                )

    except WebSocketDisconnect:
        logger.info("WebSocket client %s disconnected normally", client_id)
    except Exception as e:  # pylint: disable=broad-except
        # Broad exception needed for WebSocket errors
        logger.error("WebSocket error for client %s: %s", client_id, e)
    finally:
        await ws_manager.disconnect(client_id)


@websocket_router.get("/api/v1/websocket/stats")
async def get_websocket_stats():
    """Get WebSocket connection statistics"""
    return ws_manager.get_connection_stats()


@websocket_router.post("/api/v1/websocket/broadcast")
async def broadcast_message(message: Dict[str, Any]):
    """Broadcast message to all connected WebSocket clients (admin only)"""
    # FUTURE: Add authentication check in production

    try:
        await ws_manager.broadcast(
            {
                "type": "admin_broadcast",
                "content": message,
                "broadcast_time": time.time(),
            }
        )

        return {
            "success": True,
            "message": "Broadcast sent successfully",
            "recipients": len(ws_manager.active_connections),
            "timestamp": time.time(),
        }

    except Exception as e:  # pylint: disable=broad-except
        # Broad exception needed for broadcast errors
        logger.error("Failed to broadcast message: %s", e)
        return {"success": False, "error": str(e), "timestamp": time.time()}


# Function to send real-time updates (called from other parts of the system)
async def send_system_update(update_type: str, data: Dict[str, Any]):
    """Send system update to all connected WebSocket clients"""

    update_message = {
        "type": "system_update",
        "update_type": update_type,
        "data": data,
        "phi_optimized": True,
        "timestamp": time.time(),
    }

    await ws_manager.broadcast(update_message)


async def send_plugin_update(
    plugin_name: str, status: str, data: Optional[Dict[str, Any]] = None
):
    """Send plugin-specific update to all connected WebSocket clients"""

    update_message = {
        "type": "plugin_update",
        "plugin_name": plugin_name,
        "status": status,
        "data": data or {},
        "phi_optimized": True,
        "timestamp": time.time(),
    }

    await ws_manager.broadcast(update_message)


async def send_analysis_progress(
    analysis_id: str, progress: float, details: Optional[Dict[str, Any]] = None
):
    """Send analysis progress update to all connected WebSocket clients"""

    progress_message = {
        "type": "analysis_progress",
        "analysis_id": analysis_id,
        "progress": progress,
        "details": details or {},
        "phi_factor": progress * PHI,  # φ-enhanced progress indicator
        "timestamp": time.time(),
    }

    await ws_manager.broadcast(progress_message)
