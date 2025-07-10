"""Test AAR API Functionality"""

import os
import sys
import unittest

from fastapi.testclient import TestClient

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api.main import app


class TestAARAPI(unittest.TestCase):
    """Test AAR API endpoints and functionality"""

    def setUp(self):
        """Set up test client"""
        self.client = TestClient(app)
        self.test_user = {"username": "admin", "password": "sacred_geometry_2025"}

    def test_auth_endpoints(self):
        """Test authentication endpoints"""
        # Test login
        response = self.client.post("/api/v1/auth/login", json=self.test_user)
        self.assertEqual(response.status_code, 200)
        token_data = response.json()
        self.assertIn("access_token", token_data)
        self.assertTrue(token_data["phi_optimized"])

        # Test token verification
        headers = {"Authorization": f"Bearer {token_data['access_token']}"}
        response = self.client.get("/api/v1/auth/verify", headers=headers)
        self.assertEqual(response.status_code, 200)
        verify_data = response.json()
        self.assertTrue(verify_data["valid"])
        self.assertEqual(verify_data["user"], "admin")

    def test_plugin_endpoints(self):
        """Test plugin management endpoints"""
        # Login first
        response = self.client.post("/api/v1/auth/login", json=self.test_user)
        token = response.json()["access_token"]
        headers = {"Authorization": f"Bearer {token}"}

        # Test list plugins
        response = self.client.get("/api/v1/plugins", headers=headers)
        self.assertEqual(response.status_code, 200)
        plugins = response.json()
        self.assertTrue(isinstance(plugins, list))
        if plugins:
            plugin = plugins[0]
            self.assertIn("name", plugin)
            self.assertIn("sacred_geometry_score", plugin)

        # Test plugin execution
        plugin_request = {
            "input_data": {"test": "data"},
            "parameters": {"phi_optimized": True},
        }
        response = self.client.post(
            "/api/v1/plugins/auth_plugin/execute", headers=headers, json=plugin_request
        )
        self.assertEqual(response.status_code, 200)
        result = response.json()
        self.assertTrue(result["success"])
        self.assertGreater(result["sacred_geometry_score"], 0)

    def test_unauthorized_access(self):
        """Test unauthorized access attempts"""
        # Try accessing protected endpoint without token
        response = self.client.get("/api/v1/plugins")
        self.assertEqual(response.status_code, 401)

        # Try login with invalid credentials
        response = self.client.post(
            "/api/v1/auth/login", json={"username": "invalid", "password": "invalid"}
        )
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
