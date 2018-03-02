#!/usr/bin/python
## python template
import numpy as np
from numpy import arange

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
                vec[j] = vec[j]/this.val[j,j]
                for i in np.arange(j+1,this.n):
                    vec[i] = vec[i] - this.val[i,j]*vec[j]
                # end for 'i'
            else:
                return -1    
            # end if
        # end for 'j'
        
        for j in np.arange(this.n-1,-1,-1):
            if this.val[j,j] != 0.0:
                vec[j] = vec[j]/this.val[j,j]
                for i in np.arange(0,j):
                    vec[i] = vec[i] - this.val[j,i]*vec[j]
                # end for 'i'
            else:
                return -1    
            # end if
            
        # end for 'j'


        
        #return vec
    # end of solve


    def set_matrix(this):
        this.val[0,0]=  3
        this.val[0,1]= -1
        this.val[0,2]= -1
        this.val[1,0]= -1
        this.val[1,1]=  3
        this.val[1,2]= -1
        this.val[2,0]= -1
        this.val[2,1]= -1
        this.val[2,2]=  3
    # end of set_matrix
    
    def cholesky(this):
        for k in np.arange(0,this.n):
            this.val[k,k] = np.sqrt(this.val[k,k])
            
            for i in np.arange(k+1,this.n):
                this.val[i,k] = this.val[i,k]/this.val[k,k]
            # end for 'i'            
            
            for j in np.arange(k+1,this.n):
                for i in np.arange(j,this.n):
                    this.val[i,j] = this.val[i,j] - this.val[i,k]*this.val[j,k]
                # end for 'i'            
            # end for 'j'            
        # end for 'k'            
    # end of cholesky
    
    def print_matrix(this):
        print this.val
    # end of print_matrix
    
# end of class MyClass    


def main():
    
    n=3
    x=np.zeros((n), dtype=float)
    x[0]= -651.0
    x[1]= 2177.0
    x[2]= 4069.0
    
    
    print ("This is main")
    a=Matrix(n)
    a.set_matrix()
    a.print_matrix()
    print x
    a.cholesky()
    a.solve(x)
    print
    print
    a.print_matrix()
    print
    print x
    return (0)
# end of main()    
    
if __name__ == '__main__':
    main()
# end if
