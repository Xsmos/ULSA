from ULSA.sky_map.produce_absorbed_sky_map import absorption_JRZ
import healpy as hp
import numpy as np
import matplotlib.pyplot as plt

def produce_sky_map():
    sky_map_list = []
    nside = 2 ** 6
    dist = 50.

    for v in range(1,10,1):
        f = absorption_JRZ(v=v, nside=nside, index_type='constant_index', distance=dist,
                           using_raw_diffuse=False, using_default_params=False, input_spectral_index=None,
                           critical_dis=False, output_absorp_free_skymap=False)
        sky_map_list.append(f.mpi())

    return sky_map_list

def plot():
    sky_map_list = produce_sky_map()
    plt.figure()
    for sky_map in sky_map_list:
        hp.mollview(np.log10(sky_map), cmap = plt.cm.jet)
        plt.show()

plot()