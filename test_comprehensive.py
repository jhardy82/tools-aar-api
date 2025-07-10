"""Comprehensive AAR API Testing"""

import requests

# Test configuration
BASE_URL = "http://localhost:8000"
TEST_USER = {"username": "admin", "password": "sacred_geometry_2025"}


def test_root_endpoint():
    """Test root endpoint"""
    print("🔍 Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Root endpoint working - Version: {data.get('version')}")
        print(f"   φ constant: {data.get('phi_constant')}")
        return True
    else:
        print(f"❌ Root endpoint failed: {response.text}")
        return False


def test_system_status():
    """Test system status endpoint"""
    print("\n🔍 Testing system status...")
    response = requests.get(f"{BASE_URL}/api/v1/system/status")
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print("✅ System status working")
        print(f"   Status: {data.get('status')}")
        print(f"   Sacred Geometry Score: {data.get('sacred_geometry_score')}")
        print(f"   Plugin Count: {data.get('plugin_count')}")
        return True
    else:
        print(f"❌ System status failed: {response.text}")
        return False


def test_authentication():
    """Test authentication endpoints"""
    print("\n🔍 Testing authentication...")

    # Test login
    response = requests.post(
        f"{BASE_URL}/api/v1/auth/login",
        json=TEST_USER,
        headers={"Content-Type": "application/json"},
    )
    print(f"Login Status: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print("✅ Login successful")
        print(f"   Token type: {data.get('token_type')}")
        print(f"   φ-optimized: {data.get('phi_optimized')}")
        print(f"   Expires in: {data.get('expires_in')} seconds")

        token = data.get("access_token")

        # Test token verification
        headers = {"Authorization": f"Bearer {token}"}
        verify_response = requests.get(
            f"{BASE_URL}/api/v1/auth/verify", headers=headers
        )
        print(f"Verify Status: {verify_response.status_code}")

        if verify_response.status_code == 200:
            verify_data = verify_response.json()
            print("✅ Token verification successful")
            print(f"   Valid: {verify_data.get('valid')}")
            print(f"   User: {verify_data.get('user')}")
            print(f"   Role: {verify_data.get('role')}")
            return token
        else:
            print(f"❌ Token verification failed: {verify_response.text}")
            return None
    else:
        print(f"❌ Login failed: {response.text}")
        return None


def test_plugins(token):
    """Test plugin endpoints"""
    print("\n🔍 Testing plugin endpoints...")

    if not token:
        print("❌ No token available for plugin testing")
        return False

    headers = {"Authorization": f"Bearer {token}"}

    # Test list plugins
    response = requests.get(f"{BASE_URL}/api/v1/plugins", headers=headers)
    print(f"List Plugins Status: {response.status_code}")

    if response.status_code == 200:
        plugins = response.json()
        print("✅ Plugin listing successful")
        print(f"   Found {len(plugins)} plugins")

        if plugins:
            plugin = plugins[0]
            print(f"   Plugin: {plugin.get('name')} v{plugin.get('version')}")
            print(f"   Sacred Geometry Score: {plugin.get('sacred_geometry_score')}")

            # Test plugin execution
            exec_data = {
                "input_data": {"test": "data"},
                "parameters": {"phi_optimized": True},
            }

            exec_response = requests.post(
                f"{BASE_URL}/api/v1/plugins/{plugin['name']}/execute",
                json=exec_data,
                headers=headers,
            )
            print(f"Plugin Execution Status: {exec_response.status_code}")

            if exec_response.status_code == 200:
                exec_result = exec_response.json()
                print("✅ Plugin execution successful")
                print(f"   Success: {exec_result.get('success')}")
                print(f"   Execution time: {exec_result.get('execution_time')}s")
                print(
                    f"   Sacred Geometry Score: {exec_result.get('sacred_geometry_score')}"
                )
                return True
            else:
                print(f"❌ Plugin execution failed: {exec_response.text}")
                return False
        return True
    else:
        print(f"❌ Plugin listing failed: {response.text}")
        return False


def test_unauthorized_access():
    """Test unauthorized access"""
    print("\n🔍 Testing unauthorized access...")

    # Test accessing protected endpoint without token
    response = requests.get(f"{BASE_URL}/api/v1/plugins")
    print(f"No Token Status: {response.status_code}")

    if response.status_code == 401:
        print("✅ Unauthorized access properly blocked")
        return True
    else:
        print(f"❌ Unauthorized access not blocked: {response.status_code}")
        return False


def main():
    """Run comprehensive API tests"""
    print("🌟 AAR System API Comprehensive Testing")
    print("=" * 50)

    results = []

    # Test all endpoints
    results.append(test_root_endpoint())
    results.append(test_system_status())

    token = test_authentication()
    results.append(token is not None)

    results.append(test_plugins(token))
    results.append(test_unauthorized_access())

    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    passed = sum(results)
    total = len(results)
    print(f"   Passed: {passed}/{total}")
    print(f"   Success Rate: {(passed/total)*100:.1f}%")

    if passed == total:
        print("🎉 All tests passed! AAR API is fully functional.")
    else:
        print("⚠️ Some tests failed. Check the output above for details.")

    return passed == total


if __name__ == "__main__":
    try:
        success = main()
        exit(0 if success else 1)
    except Exception as e:
        print(f"❌ Test execution failed: {e}")
        exit(1)
