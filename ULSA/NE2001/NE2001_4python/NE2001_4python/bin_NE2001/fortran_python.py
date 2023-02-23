import ctypes as ct
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# import the dll
libNE2001 = ct.CDLL('../src.NE2001/libNE2001.so')
rad=57.2957795
#radian per degree

#distance equals 50kpc
dist=50.0

# setup the data
N =np.int(dist/0.01)

print ('N',N)

nd = ct.pointer( ct.c_int(N) )          # setup the pointer

em1D = np.arange(0, N, dtype=np.float32)  # setup the N-long

l = 0.0
b = 65.0


l = l * np.pi/180. #now its radian unit
b = b * np.pi/180.


_ = libNE2001.em_los_(nd, ct.pointer( ct.c_float(l) ), ct.pointer( ct.c_float(b) ), ct.pointer( ct.c_float(dist) ), np.ctypeslib.as_ctypes(em1D))

Te = 8000.
v = 1e6
Tao_mw = 3.28*1e-7 * (Te/1e4)**-1.35 * (v * 1e-9)**-2.1 * em1D
print ('l in radian unit',l,'b in radian unit',b)
print ('exp(-tao)_to 0.1kpc and 50kpc',np.exp(-Tao_mw[0]),np.exp(-Tao_mw[-1]),em1D.shape)
print ('EM_to 0.1kpc and 50kpc',em1D[0],em1D[-1])
print ('optical_depth_to 0.1kpc and 50kpc',Tao_mw[0],Tao_mw[-1])

# call the function by passing the ctypes pointer using the numpy function:
def loop():
    plt.figure()
    for l in range(0,360,30):
        b = 15.
        l = l * np.pi/180. #now its radian unit
        b = b * np.pi/180.


        _ = libNE2001.em_los_(nd, ct.pointer( ct.c_float(l) ), ct.pointer( ct.c_float(b) ), ct.pointer( ct.c_float(dist) ), np.ctypeslib.as_ctypes(em1D))

        Te = 8000.
        v = 1e6
        Tao_mw = 3.28*1e-7 * (Te/1e4)**-1.35 * (v * 1e-9)**-2.1 * em1D
        X = np.arange(0,50,0.01)
        plt.plot(X,Tao_mw,label = 'l:'+str(np.round(l*180/np.pi,2))+'_b'+str(np.round(b*180./np.pi,2)))
    plt.xlim(0,2)
    plt.xlabel('R (kpc)')
    plt.ylabel('Optical depth in 1Mhz')
    plt.legend(loc='best')
    plt.savefig('linshi.png')
    return 
loop()     
#_ = fortlib.sqr_1d_arr_(nd, np.ctypeslib.as_ctypes(pyarr))

