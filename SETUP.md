# AAR API Setup Instructions

## Sacred Geometry Framework - FastAPI Implementation

### Prerequisites
- Python 3.9 or higher
- Virtual environment (recommended)

### Installation

1. **Create and activate virtual environment:**
```bash
python -m venv aar-api-env
# Windows
aar-api-env\Scripts\activate
# Linux/Mac
source aar-api-env/bin/activate
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up environment variables (production):**
```bash
export JWT_SECRET_KEY="your-secret-key-here"
export DATABASE_URL="your-database-url"
export ENVIRONMENT="production"
```

### Development Setup

1. **Install additional development dependencies:**
```bash
pip install pytest pytest-asyncio pytest-mock httpx black flake8 mypy
```

2. **Run the application:**
```bash
python main.py
```

The API will be available at:
- Main API: http://localhost:8000
- Interactive docs: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Local Module Dependencies

The application expects these local modules to be available:
- `modules.plugins.manager` - Plugin management system
- `modules.config.manager` - Configuration management
- `modules.utils.safe_logging` - Safe logging utilities

If these modules are not available, the application will run in fallback mode with basic logging.

### Sacred Geometry Features

The API implements Sacred Geometry principles:
- **φ (Golden Ratio)**: Token expiration, rate limiting optimization
- **Circle**: Complete request-response lifecycle
- **Triangle**: Three-tier security validation
- **Spiral**: Progressive API enhancement
- **Fractal**: Self-similar endpoint patterns

### API Endpoints

- `GET /` - API information and Sacred Geometry metrics
- `GET /api/v1/system/status` - System status with φ-optimization score
- `WebSocket /ws` - Real-time updates with φ-optimized heartbeat

### Testing

```bash
pytest tests/ -v
```

### Production Deployment

1. Set proper environment variables
2. Use a production WSGI server (gunicorn with uvicorn workers)
3. Configure proper CORS origins
4. Set up SSL/TLS certificates
5. Configure rate limiting with Redis
6. Set up monitoring and logging

### Security Notes

- Change JWT_SECRET_KEY in production
- Configure allowed hosts properly
- Use HTTPS in production
- Implement proper authentication backend
- Review CORS settings for production use
