#
# Makefile for NE2001
# 
# Edit the initial variables for your system.
# Then type 'make pgm' to make the NE2001 interface 
# or        'make lib' to meke the library.
#
FC      = f77
#FC=ifort
RANLIB  = ranlib
ARFLAGS = rc
FFLAGS  = -O -ffixed-line-length-132
LDFLAGS = -s
#
BINDIR = ../bin.NE2001
#
# Nothing below here should need to be changed.
########################################################################
PROGRAM = NE2001
OBJECTS = dmdsm.NE2001.o density.NE2001.o neLISM.NE2001.o neclumpN.o \
		nevoidN.o scattering98.o

OBJECTS2 = dmdsm.NE2001.f density.NE2001.f neLISM.NE2001.f neclumpN.f \
		nevoidN.f scattering98.f


usage:
	@echo 'Please type one of the following:'
	@echo 'make pgm --- to make the NE2001 interface'
	@echo 'make lib --- to make the Fortran library'

all: pgm lib

pgm: $(PROGRAM)

lib: lib$(PROGRAM).a

so: lib$(PROGRAM).so

$(PROGRAM): $(PROGRAM).o $(OBJECTS)
	$(FC) $(FFLAGS) $(LDFLAGS) -o $(BINDIR)/$(PROGRAM) $(PROGRAM).o $(OBJECTS)

lib$(PROGRAM).a: $(OBJECTS)
	$(AR) $(ARFLAGS) $@ $(OBJECTS)
	$(RANLIB) $@

lib$(PROGRAM).so: $(OBJECTS2)
	$(FC) $(FFLAGS) $(LDFLAGS) -shared -fPIC  -g -o lib$(PROGRAM).so $(OBJECTS2)




NE2001.o: NE2001.f 

density.NE2001.o: density.NE2001.f

neLISM.NE2001.o: neLISM.NE2001.f

neclumpN.o: neclumpN.f

nevoidN.o: nevoidN.f

dmdsm.NE2001.o: dmdsm.NE2001.f

scattering98.o: scattering98.f

clean: 
	$(RM) $(BINDIR)/$(PROGRAM) $(PROGRAM).o $(OBJECTS) lib$(PROGRAM).so
