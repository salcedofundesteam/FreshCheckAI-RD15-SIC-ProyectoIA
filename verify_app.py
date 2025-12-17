import threading
import time
import requests
import sys
from app import app

def run_server():
    app.run(port=5000, debug=False, use_reloader=False)

def verify():
    # Start server in a separate thread
    thread = threading.Thread(target=run_server)
    thread.daemon = True
    thread.start()
    
    # Wait for server to start
    print("Waiting for server to start...")
    time.sleep(5)
    
    try:
        # Test main page
        response = requests.get('http://127.0.0.1:5000/')
        if response.status_code == 200:
            print("SUCCESS: Main page loaded successfully.")
        else:
            print(f"FAILURE: Main page returned {response.status_code}")
            sys.exit(1)
            
        print("Verification complete!")
        
    except Exception as e:
        print(f"FAILURE: Could not connect to server. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    verify()
