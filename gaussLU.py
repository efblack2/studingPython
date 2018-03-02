#!/usr/bin/python
## python template
import numpy as np
from numpy import arange
import sys


class Matrix:
    '''
        variables
    '''
    n = 0

    def __init__(this, _n):  # This is the Constructor
        print "hello form constructor"
        this.n = _n
        this.val = np.zeros((this.n,this.n), dtype=float)
    # end of __init__() constructor
    
    def __del__(this):  # This is the Destructor
        print 'bye form destructor'
    # end of __del__() destructor

    def print_size(this):
        print this.n
    # end of print_a
    
    def solve(this, vec):
        for j in np.arange(0,this.n):
            if this.val[j,j] != 0.0:
                #vec[j] = vec[j]/this.val[j,j]
                for i in np.arange(j+1,this.n):
                    vec[i] = vec[i] - this.val[i,j]*vec[j]
                # end for 'i'
            else:
                print 'Singular matrix. Exiting....'
                sys.exit()
            # end if
        # end for 'j'
        
        for j in np.arange(this.n-1,-1,-1):
            if this.val[j,j] != 0.0:
                vec[j] = vec[j]/this.val[j,j]
                for i in np.arange(0,j):
                    vec[i] = vec[i] - this.val[i,j]*vec[j]
                # end for 'i'
            else:
                print 'Singular matrix. Exiting....'
                sys.exit()
            # end if
        # end for 'j'
        


        
        #return vec
    # end of solve


    def set_matrix(this):
        this.val[0,0]=  1.0
        this.val[0,1]=  2.0
        this.val[0,2]=  2.0
        
        this.val[1,0]= 4.0
        this.val[1,1]= 4.0
        this.val[1,2]= 2.0
        
        this.val[2,0]= 4.0
        this.val[2,1]= 6.0
        this.val[2,2]= 4.0
        
    # end of set_matrix
    
    def gaussLU(this):        
        for k in np.arange(0,this.n-1):
            if (this.val[k,k] != 0):
                for row in np.arange(k+1,this.n):
                    m = this.val[row,k]/this.val[k,k]
                    this.val[row,k] =  m 
                # end for 'row'
                for col in np.arange(k+1,this.n):
                    for row in np.arange(k+1,this.n):
                        this.val[row,col] = this.val[row,col] - m * this.val[k,col] 
                    # end for 'row'
                # end for 'row'
            else:
                print 'exiting....'
                sys.exit()
            # end if
    # end of gaussLU
    
    def print_matrix(this):
        print this.val
    # end of print_matrix
    
# end of class MyClass    


def main():
    
    n=3
    b=np.zeros((n), dtype=float)
    b[0]= 3.0
    b[1]= 6.0
    b[2]= 10.0
    
    
    print ("This is main")
    a=Matrix(n)
    a.set_matrix()
    a.print_matrix()
    print b
    a.gaussLU()
    a.print_matrix()
    a.solve(b)
    print
    print
    a.print_matrix()
    print
    print b
    return (0)
# end of main()    
    
if __name__ == '__main__':
    main()
# end if
