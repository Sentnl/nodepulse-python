from nodepulse import NodePulse
import requests

def check_ipfs_gateway(node):
    # Test CID that should always be available
    test_cid = "QmWnfdZkwWJxabDUbimrtaweYF8u9TaESDBM8xvRxxbQxv"
    try:
        response = requests.get(
            f"{node}/ipfs/{test_cid}",
            headers={'Range': 'bytes=0-0'},  # Only get first byte
            timeout=5
        )
        if response.status_code in [200, 206]:  # 206 for partial content
            print(f"✅ IPFS gateway {node} is healthy")
            return True
        else:
            print(f"❌ IPFS gateway {node} returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error checking IPFS gateway {node}: {str(e)}")
        return False

# Initialize NodePulse for IPFS
node_pulse = NodePulse(
    node_type='ipfs',
    network='mainnet',
    node_count=3,
    update_interval=10000  # Set to 10 seconds for testing
)

# Get a node and test it
node = node_pulse.get_node()
check_ipfs_gateway(node) 