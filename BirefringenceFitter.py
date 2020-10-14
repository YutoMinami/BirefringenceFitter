import numpy as np

class BirefringenceFitter:
	def __init__(self, powvecs, cmb_powvecs, covmatrices, ):
		self.alphas = np.zeros(powvecs.shape[0])
		self.beta = 0.0


	def PrepareAlphaTemplates(self):
		self.alpha_temp01 = np.zeros((self.powvecs.shape[0], len(self.name_list)),dtype =float)
		self.alpha_temp02 = np.zeros((self.powvecs.shape[0], len(self.name_list)),dtype =float)
		for i,comb in enumerate(self.combs_cov):
			self.alpha_temp01[i][comb[0]] = 2.
			self.alpha_temp02[i][comb[1]] = 2.
		self.alpha_sum  = self.alpha_temp01 + self.alpha_temp02
		self.alpha_diff = self.alpha_temp01 - self.alpha_temp02
		self.alpha_temp = np.ones(( self.powvecs.shape[0]  , len(self.Fitmodes) ),dtype =float)
		self.alpha_temp[:,0]*=-1

	def PrepareAlphaVecs(self):
		self.alphavecs = np.copy(self.alpha_temp)
		self.alphavecs.T[0:2,:] *= 1./np.cos(self.alpha_sum @ self.alphas)/ np.cos(self.alpha_diff@ self.alphas) 
		self.alphavecs[:,0] *= np.sin( 2*self.alpha_temp02 @ self.alphas) /2.
		self.alphavecs[:,1] *= np.sin( 2*self.alpha_temp01 @ self.alphas) /2.
	def PrepareBetaVecs(self):
	name_list, XFT_list, inpowname, powvec_name, covname ,nside =512 ,lmin=2,lmax= 1024,  bins=None ,
	isOnlyDiag =False, negEBEB = False, negEBXX = 0, 
	withVarCMB = False, isSimple = False, fwhm_list = None
	):
	
