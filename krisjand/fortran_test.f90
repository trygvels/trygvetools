program test
  implicit none

  real           :: radius, vec(3), gal(2), pi
  integer        :: i, stat
  integer   :: len_file
  character(len=512) :: partext, line, sourcefile
  character(len=3)   :: test_str

  pi = 3.141592
  call  getarg(1,sourcefile)
!  sourcefile = 'test_dir/sources.txt'
  open(1,file=sourcefile)                                                                  
                                                                               
  do                                                                           
     read(1, '(a)', IOSTAT=stat) line                                             
     if (stat > 0) then                                                            
        write(*,*) "Something went wrong while trying to read the file"          
        exit                                                                  
     end if
     if (stat < 0) exit !end of file reached                                    
     write(*,*) 'line: ',line
     !test_str='123456'
     !write(*,*) 'test_str: ',test_str(2:3)
     !else we extract the source data                     
     line=trim(line) 
     !test_str=line(1)
     if ( line(1:1) == '#' ) cycle ! a commented line                          
     read(line,*) gal(1),gal(2),radius,partext                         
     !galactic coord -> spherical coord                       
     write(*,*) 'gal: ', gal(:)
     write(*,*) 'rad: ', radius
     write(*,*) 'com: ', trim(partext)
     gal(1) = 90.d0 - gal(1)
     radius = radius/60.d0 * pi/180.d0 

  end do

  call get_len_of_file(sourcefile,len_file)
  write(*,*) 'Length of file:', len_file, 'lines'
end program test

subroutine get_len_of_file(filename,len)
  implicit none 
  character(len=512)         :: filename
  character(len=512)         :: line
  character(len=128), allocatable, dimension(:)   :: line_arr
  integer, intent(out)  :: len
  integer                    :: stat

  open(3,file=filename)
  len=0
  do
     read(3,'(a)', IOSTAT=stat) line
     if (stat > 0) then                                                            
        write(*,*) "Something went wrong while trying to read the file"          
        exit                                                                  
     end if
     if (stat < 0) exit !end of file reached                                    
     len = len + 1
  end do

  allocate(line_arr(len))
  call some_bull(len)
end subroutine get_len_of_file

subroutine some_bull(length, arr2)
  implicit none
  integer :: length
  character(len=128), allocatable, dimension(:), intent(out) :: arr2(length)
  integer :: i
  do i = 1,length
     write(arr2(i),'(a)') i
     write(*,*) arr2(i)
  end do


end subroutine some_bull
