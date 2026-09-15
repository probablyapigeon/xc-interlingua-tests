# xc-test:name=linear_4d
# xc-test:category=semantic-equivalence
# xc-test:expressible=true
# xc-test:state_dim=4
# xc-test:cycles=4
# xc-test:operator_complexity=linear
# xc-test:memory_capacity=0
# xc-test:policy_actions=2
# xc-test:measure_count=2
state x[4]
operator step = tanh(Wx + b)
policy select = argmax(measure)
