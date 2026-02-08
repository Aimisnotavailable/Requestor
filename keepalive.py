import requests
import time
import argparse
from datetime import datetime

def send_ping(url):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        response = requests.get(url, timeout=10)
        print(f"[{now}] Request sent to {url} | Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[{now}] Failed to reach server. Error: {e}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Periodically ping a server URL.")
    
    # Adding the --url argument
    parser.add_argument(
        "--url", 
        type=str, 
        required=True, 
        help="The full URL to request (e.g., https://google.com)"
    )
    
    # Adding an optional --interval argument (defaulted to 120 seconds)
    parser.add_argument(
        "--interval", 
        type=int, 
        default=120, 
        help="Time between requests in seconds (default: 120)"
    )

    args = parser.parse_args()

    print(f"--- Starting Pinger ---")
    print(f"Target: {args.url}")
    print(f"Interval: {args.interval} seconds")
    print("Press Ctrl+C to stop.")
    print("-----------------------")

    try:
        while True:
            send_ping(args.url)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nScript stopped. Have a productive day!")

if __name__ == "__main__":
    main()
