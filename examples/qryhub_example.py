from nodepulse import NodePulse

# Initialize NodePulse with QryHub options
node_pulse = NodePulse(
    use_qry_hub=True,
    chain_id='73e4385a2708e6d7048834fbc1079f2fabb17b3c125b146af438971e90716c4d',
    node_type='hyperion',
    node_count=3,
    history_full=True,
    streaming_enabled=True
)

# Get a node
node = node_pulse.get_node()
print(f"\nUsing QryHub node: {node}") 