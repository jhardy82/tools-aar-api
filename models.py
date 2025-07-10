"""API Models Module"""

from typing import Any, Dict, Optional

from pydantic import BaseModel, Field


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
