#!/usr/bin/env python3
"""
Test script for the Student Reading Score Prediction API
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_api():
    """Test all API endpoints"""
    
    print("🧪 Testing Student Reading Score Prediction API...")
    print("=" * 60)
    
    # Test root endpoint
    print("\n1️⃣ Testing API Information Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Failed: {e}")
    
    # Test health check
    print("\n2️⃣ Testing Health Check Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Failed: {e}")
    
    # Test model info
    print("\n3️⃣ Testing Model Information Endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/model-info")
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Failed: {e}")
    
    # Test prediction
    print("\n4️⃣ Testing Prediction Endpoint...")
    test_student = {
        "gender": "female",
        "ethnic_group": "group B",
        "parent_educ": "bachelor's degree",
        "lunch_type": "standard",
        "test_prep": "completed",
        "parent_marital_status": "married",
        "practice_sport": "regularly",
        "is_first_child": "yes",
        "nr_siblings": 2.0,
        "transport_means": "private",
        "wkly_study_hours": "5 - 10",
        "math_score": 85.0,
        "writing_score": 88.0
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=test_student,
            headers={"Content-Type": "application/json"}
        )
        print(f"✅ Status: {response.status_code}")
        print(f"📝 Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"❌ Failed: {e}")
    
    print("\n" + "=" * 60)
    print("🎯 API Testing Complete!")

if __name__ == "__main__":
    print("⏳ Waiting for API server to start...")
    time.sleep(2)  # Give server time to start
    test_api()
