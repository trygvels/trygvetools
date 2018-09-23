F90=ifort
FFLAGS=-g -C -qopenmp -traceback

paramfile : create_comm2_parameter_file.f90
	$(F90) $(FFLAGS) -o create_param create_comm2_parameter_file.f90 

test : fortran_test.f90
	$(F90) $(FFLAGS) -o fortran_test fortran_test.f90 

clean_param :
	rm *.mod create_param *~

clean_test :
	rm *.mod fortran_test *~
