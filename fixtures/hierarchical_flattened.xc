# xc-test:name=hierarchical_flattened
# xc-test:category=expressiveness-boundaries
# xc-test:expressible=true
# xc-test:state_dim=32
# xc-test:cycles=4
# xc-test:operator_complexity=nested-calls
# xc-test:memory_capacity=1
# xc-test:policy_actions=8
# xc-test:measure_count=5
state root.child_a[16]
state root.child_b[16]
operator flatten = compose(branch_a, branch_b)
