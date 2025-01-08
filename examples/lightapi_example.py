from nodepulse import NodePulse
import requests

def check_lightapi_status(node):
    try:
        response = requests.get(f"{node}/api/status", timeout=5)
        if response.status_code == 200 and response.text.strip() == "OK":
            print(f"✅ LightAPI node {node} is healthy")
            return True
        else:
            print(f"❌ LightAPI node {node} returned unexpected response")
            return False
    except Exception as e:
        print(f"❌ Error checking LightAPI node {node}: {str(e)}")
        return False

# Initialize NodePulse for LightAPI
node_pulse = NodePulse(
    node_type='lightapi',
    network='mainnet',
    node_count=3,
    update_interval=10000  # Set to 10 seconds for testing
)

# Get a node and test it
node = node_pulse.get_node()
check_lightapi_status(node) 