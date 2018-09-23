program parameter_file
  implicit none
  integer            :: i,j
  double precision   :: data
  character(len=200) :: inline
  character(len=200), dimension(10)  :: line_arr

  do i = 1,10
     write(line_arr,'(a,I0)') "i = ",i
     write(*,*) trim(line_arr(i))
     write(*,*) i, "hi"
  end do

  write(*,*) "hello world"


end program parameter_file
