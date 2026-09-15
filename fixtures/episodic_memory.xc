# xc-test:name=episodic_memory
# xc-test:category=structural-invariants
# xc-test:expressible=true
# xc-test:state_dim=16
# xc-test:cycles=6
# xc-test:operator_complexity=memory-decay
# xc-test:memory_capacity=10
# xc-test:policy_actions=4
# xc-test:measure_count=5
state m[16]
memory episodic[10]
operator retrieve = tanh(query + decay)
