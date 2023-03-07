import h5py
import healpy as hp
import numpy as np
import matplotlib.pyplot as plt

with h5py.File('exp9MHz_sky_map_with_absorption.hdf5', 'r') as f:
    data = f['data']
    print(f.keys())
    print(data)
    hp.mollview(
    np.log(data),
    cmap=plt.cm.jet,
    title="sky_map_with_absorption",
    unit=r"$\log_{10}(T/\mathrm{K})$",
    norm='hist')
    hp.graticule()
    plt.savefig("exp9.png")
