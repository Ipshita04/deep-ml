def bayes_theorem(priors: list[float], likelihoods: list[float]) -> list[float]:
	"""
	Calculate posterior probabilities using Bayes' Theorem.
	
	Args:
		priors: Prior probabilities P(H_i) for each hypothesis
		likelihoods: Likelihoods P(E|H_i) for each hypothesis
		
	Returns:
		Posterior probabilities P(H_i|E) for each hypothesis
	"""
	n=len(priors)
	total=0
	ans=[]
	for i in range(n):
		total+=(priors[i]*likelihoods[i])
	for i in range(n):
		ans.append((priors[i]*likelihoods[i])/total)
	return ans	
	pass