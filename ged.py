import numpy as np 
import scipy
from matplotlib import pyplot as plt 

### Working with the Generalized Error Distribution.

def logLikelihood(obsVec, mu, cov, kappa):

    obsDim = len(mu)
    invCov = np.linalg.inv(cov)
    detCov = np.linalg.det(cov)

    negLogLike = np.log(scipy.special.gamma(1+obsDim*kappa) / scipy.special.gamma(1+0.5*obsDim))
    negLogLike += obsDim * 0.5 * np.log(np.pi/kappa*scipy.special.gamma(1+obsDim*kappa)/scipy.special.gamma((obsDim+2)*kappa))
    negLogLike += 1 / 2 * np.log(detCov)

    temp = kappa * scipy.special.gamma((obsDim+2)*kappa) / scipy.special.gamma(1+obsDim*kappa)
    z = obsVec - mu
    temp = temp * np.dot(np.dot(z.T,invCov),z)[0,0]
    temp = temp ** (1/2/kappa)
    negLogLike += temp

    return(-negLogLike)



obsVec = 0 * np.eye(1)
kappa = np.linspace(15,35, 10)
muMult = np.linspace(-2.5,2.5,1001)

logLikes = np.zeros([len(kappa),len(muMult)], dtype=np.float64)

for i in range(len(kappa)):
    for j in range(len(muMult)):
        logLikes[i,j] = logLikelihood(obsVec, muMult[j]*np.ones([1,1], dtype=np.float64), np.eye(1), kappa[i])
        
for i in range(len(kappa)):
    plt.plot(muMult, logLikes[i,:]) 
plt.legend(kappa, loc='right', title='kappa Parameter')
plt.title("Log Likelihood of 1-D GED with Identity Cov v. Mu")
plt.xlabel("mu")
plt.ylabel("Log Likelihood")
plt.grid(True)
plt.show()