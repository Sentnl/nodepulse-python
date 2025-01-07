from nodepulse import NodePulse
import logging
import time

# Setup logging
logging.basicConfig(
    level=logging.INFO,  # Changed to INFO to reduce noise
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def on_node_update(nodes):
    print(f"\nNodes updated: {[node['url'] for node in nodes]}")

def on_error(error):
    print(f"\nError occurred: {str(error)}")

def on_fallback(fallback_type, nodes):
    print(f"\nFalling back to {fallback_type} nodes: {nodes}")

# Initialize NodePulse with default options
node_pulse = NodePulse(
    node_type='hyperion',
    network='mainnet',
    node_count=3,
    update_interval=10000,  # Set to 10 seconds for testing
    log_level='info',
    on_node_update=on_node_update,
    on_error=on_error,
    on_fallback=on_fallback
)

# Get a node
node = node_pulse.get_node()
print(f"\nUsing node: {node}")

# Keep the program running to see background updates
try:
    print("\nWaiting for updates (press Ctrl+C to exit)...")
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nExiting...") 