# xc-test:name=nonlinear_policy
# xc-test:category=semantic-equivalence
# xc-test:expressible=true
# xc-test:state_dim=8
# xc-test:cycles=5
# xc-test:operator_complexity=tanh-composition
# xc-test:memory_capacity=0
# xc-test:policy_actions=4
# xc-test:measure_count=3
state h[8]
operator gate = tanh(Uh + b)
policy choose = argmax(scores)
