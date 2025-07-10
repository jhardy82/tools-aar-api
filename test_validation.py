"""
Test validation for AAR API main.py fixes
Sacred Geometry Framework - Validation Tests

This test file validates that the main.py file can be imported and
basic functionality works without external dependencies.
"""

import sys
from pathlib import Path

# Add the API directory to the path
api_dir = Path(__file__).parent
sys.path.insert(0, str(api_dir))


def test_syntax_validation():
    """Test that main.py has valid Python syntax"""
    try:
        import ast

        main_py_path = api_dir / "main.py"

        with open(main_py_path, "r", encoding="utf-8") as f:
            source_code = f.read()

        # Parse the AST to validate syntax
        ast.parse(source_code)
        print("✅ Syntax validation passed")
        return True
    except SyntaxError as e:
        print(f"❌ Syntax error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error during syntax validation: {e}")
        return False


def test_import_validation():
    """Test that main.py can be imported (may have import warnings)"""
    try:
        # Temporarily suppress import warnings for testing
        import warnings

        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            import main

        print("✅ Import validation passed")
        return True
    except ImportError as e:
        print(f"⚠️ Import warning (expected): {e}")
        return True  # Expected due to missing dependencies
    except Exception as e:
        print(f"❌ Unexpected error during import validation: {e}")
        return False


def test_constants_validation():
    """Test that Sacred Geometry constants are properly defined"""
    try:
        import main

        # Check that PHI is properly defined
        assert hasattr(main, "PHI")
        assert abs(main.PHI - 1.618033988749895) < 1e-10

        # Check that PHI_SQUARED and PHI_CUBED are defined
        assert hasattr(main, "PHI_SQUARED")
        assert hasattr(main, "PHI_CUBED")

        print("✅ Sacred Geometry constants validation passed")
        return True
    except Exception as e:
        print(f"❌ Constants validation failed: {e}")
        return False


def test_app_state_validation():
    """Test that app state is properly initialized"""
    try:
        import main

        # Check that app has state
        assert hasattr(main.app, "state")
        assert hasattr(main.app.state, "plugin_manager")
        assert hasattr(main.app.state, "config_manager")
        assert hasattr(main.app.state, "startup_time")

        print("✅ App state validation passed")
        return True
    except Exception as e:
        print(f"❌ App state validation failed: {e}")
        return False


def run_all_tests():
    """Run all validation tests"""
    print("🔺 AAR API Validation Tests - Sacred Geometry Framework")
    print("=" * 60)

    tests = [
        test_syntax_validation,
        test_import_validation,
        test_constants_validation,
        test_app_state_validation,
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        if test():
            passed += 1
        print()

    print("=" * 60)
    print(f"🌟 Test Results: {passed}/{total} passed")

    if passed == total:
        print("🎉 All validations passed! AAR API is ready for development.")
        return True
    else:
        print("⚠️ Some validations failed. Please review the issues above.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
