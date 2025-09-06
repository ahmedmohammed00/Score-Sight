#!/usr/bin/env python3
"""
Train the student reading score prediction model
"""

import os
import sys

# Add the server/app directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'server', 'app'))

from model import train_model

if __name__ == "__main__":
    print("🚀 Starting Student Reading Score Model Training...")
    try:
        # Change to server directory for relative paths
        os.chdir('server')
        train_model()
        print("✅ Training completed successfully!")
    except Exception as e:
        print(f"❌ Error during training: {e}")
        sys.exit(1)
