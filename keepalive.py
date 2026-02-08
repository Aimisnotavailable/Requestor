import requests
import time
import argparse
from datetime import datetime

def perform_request(url, method):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Standard headers to mimic a real browser
    headers = {
        "User-Agent": "Python-HTTP-Pinger/1.0",
        "Accept": "*/*"
    }

    try:
        # Standardizing the method name (GET, POST, etc.)
        method = method.upper()
        
        # dynamic execution of the requests method
        response = requests.request(method, url, headers=headers, timeout=15)
        
        print(f"[{now}] {method} -> {url} | Status: {response.status_code} ({response.reason})")
        
        # If the server returns a client or server error (4xx or 5xx)
        if not response.ok:
            print(f"      Warning: Server returned an error.")

    except requests.exceptions.ConnectionError:
        print(f"[{now}] Error: Could not connect to the server. Is the URL correct?")
    except requests.exceptions.Timeout:
        print(f"[{now}] Error: The request timed out.")
    except Exception as e:
        print(f"[{now}] Unexpected Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Customizable HTTP Request Scheduler")
    
    parser.add_argument("--url", type=str, required=True, help="The target URL (e.g., http://example.com)")
    parser.add_argument("--interval", type=int, default=120, help="Interval in seconds (default: 120)")
    parser.add_argument("--method", type=str, default="GET", choices=["GET", "POST", "PUT", "DELETE", "HEAD"], 
                        help="HTTP method to use (default: GET)")

    args = parser.parse_args()

    print(f"Ping initialized: {args.method} {args.url} every {args.interval}s")
    print("Press Ctrl+C to exit safely.\n")

    try:
        while True:
            perform_request(args.url, args.method)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nScheduler stopped. Goodbye!")

if __name__ == "__main__":
    main()
