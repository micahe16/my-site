# starter — fill in the parameters
import numpy as np
rng = np.random.default_rng(seed=0)
draws = rng.binomial(8, 0.33, size=100_000)
print((draws == 3).mean())