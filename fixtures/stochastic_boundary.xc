# xc-test:name=stochastic_boundary
# xc-test:category=expressiveness-boundaries
# xc-test:expressible=false
# xc-test:state_dim=4
# xc-test:cycles=3
# xc-test:operator_complexity=stochastic
# xc-test:memory_capacity=0
# xc-test:policy_actions=2
# xc-test:measure_count=1
state x[4]
operator sample = gaussian_noise(mu, sigma)
policy select = random_choice(actions)
