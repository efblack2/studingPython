#!/usr/bin/python
## python template
import numpy as np
from numpy import arange

class Matrix:
    '''
        variables
    '''
    m = 0
    n = 0

    def __init__(this, _m, _n):  # This is the Constructor
        print "hello form constructor"
        this.m = _m
        this.n = _n
        this.val = np.zeros((this.m,this.n), dtype=float)
        this.r = np.zeros((this.n,this.n), dtype=float)
    # end of __init__() constructor
    
    def __del__(this):  # This is the Destructor
        print 'bye form destructor'
    # end of __del__() destructor

    def print_size(this):
        print this.m
        print this.n
    # end of print_a

    def set_matrix(this):
        this.val[0,0]=  1
        this.val[1,0]=  0
        this.val[2,0]=  0
        this.val[3,0]= -1
        this.val[4,0]= -1
        this.val[5,0]=  0
        
        this.val[0,1]=  0
        this.val[1,1]=  1
        this.val[2,1]=  0
        this.val[3,1]=  1
        this.val[4,1]=  0
        this.val[5,1]= -1
        
        this.val[0,2]=  0
        this.val[1,2]=  0
        this.val[2,2]=  1
        this.val[3,2]=  0
        this.val[4,2]=  1
        this.val[5,2]=  1        
    # end of set_matrix
    
    def print_matrix(this):
        print this.val
        print this.r
    # end of print_matrix

    def mod_gs(this, b):
        this.tmp = np.zeros((this.n), dtype=float)
        for col in np.arange(0,this.n):
            rkk=np.linalg.norm(this.val[:,col])
            this.r[col,col]=rkk
            
            if (rkk != 0):
                this.val[:,col] = this.val[:,col]/rkk
                this.tmp[col]=np.dot( this.val[:,col], b )
                for row in np.arange(col+1,this.n):
                    rkj = np.dot( this.val[:,col],this.val[:,row] )
                    this.r[col,row]=rkj
                    this.val[:,row]=this.val[:,row] - rkj*this.val[:,col]
                # end for 'row'
            # end if
        # end for 'col'
        b[0:this.n]=this.tmp;
    # end of mod_gs()
    
# end of class MyClass    

def main():

    print ("This is main")
    m=6    
    n=3
    b=np.zeros((m), dtype=float)
    b[0]= 1237
    b[1]= 1941
    b[2]= 2417
    b[3]=  711
    b[4]= 1177
    b[5]= 475
    
    A=Matrix(m,n)
    #A.print_size()
    A.set_matrix()
    A.print_matrix()
    print b
    
    A.mod_gs(b)
    
    A.print_matrix()
    
    print 'verificando A = Q * R'
    print np.matmul(A.val, A.r)
    print 'end of verificando'
    
    print b[0:n]
    
    return (0)
# end of main()    
    
if __name__ == '__main__':
    main()
# end if
