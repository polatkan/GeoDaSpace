'''
Plot performance in computing (all) LM spatial diagnostics
'''

from log_plots import load_log_py, load_log_r
import matplotlib.pylab as plt
import os

if os.uname()[0] == 'Darwin':
    print 'Running MacOSX'
    comp = '/Users/'
elif os.uname()[0] == 'Linux':
    print 'Running Linux'
    comp = '/home/'

py_link = comp + 'dani/Dropbox/aagLogs/ols_py.log'
model_py, n_py, k_py, creDa_py, creWe_py, ols_py, lm_py, moran_py, gmswls_py, stsls_py, total_py = load_log_py(py_link)
r_link = comp + 'dani/Dropbox/aagLogs/ols_r.log'
model_r, n_r, k_r, creDa_r, creWe_r, ols_r, lm_r, moran_r, gmswls_r, stsls_r, total_r = load_log_r(r_link)


reg_fig = plt.figure(1)
reg_sub = plt.subplot(111)
plt.plot(n_r[:len(lm_r)], lm_r, label='R')
plt.plot(n_py[:len(lm_py)], lm_py, label='Spreg')
plt.legend(loc=2)
plt.title("Computation time for (all) LM spatial diagnostics", weight='bold')
plt.xlabel('N')
plt.ylabel('Seconds')
plt.savefig(comp + 'dani/Dropbox/aagGraphs/lm.png')

#plt.show()
