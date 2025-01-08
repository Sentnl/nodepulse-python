from nodepulse import NodePulse
import requests
import time
import json

def check_chain_info():
    try:
        # Get a healthy node
        node = node_pulse.get_node()
        print(f"\nUsing node: {node}")

        # Get chain info
        response = requests.get(f"{node}/v1/chain/get_info")
        chain_info = response.json()
        print(f"Chain info: {json.dumps(chain_info, indent=2)}")
        
    except Exception as error:
        print(f"Failed to get chain info: {str(error)}")

# Initialize NodePulse with default options
node_pulse = NodePulse(
    node_type='hyperion',
    network='mainnet',
    node_count=3,
    update_interval=10000  # Set to 10 seconds for testing
)

# Initial check
check_chain_info()

# Keep checking every 10 seconds
try:
    print("\nChecking chain info every 10 seconds (press Ctrl+C to exit)...")
    while True:
        time.sleep(10)
        check_chain_info()
except KeyboardInterrupt:
    print("\nExiting...") 