#!/usr/bin/python
## python matrix playing
## Example 2.8 Small Residuals Heat Book.
import numpy as np

def main():
    a = np.zeros((2,2), dtype=float)
    b = np.zeros((2), dtype=float)
    x1 = np.zeros((2), dtype=float)
    x2 = np.zeros((2), dtype=float)
    r1 = np.zeros((2), dtype=float)
    r2 = np.zeros((2), dtype=float)
    
    b[0]=0.254
    b[1]=0.127
    a[0][0]=0.913
    a[0][1]=0.659
    a[1][0]=0.457
    a[1][1]=0.330
    
    x1[0]=-0.0827
    x1[1]= 0.5
    
    x2[0]=0.999
    x2[1]=-1.001
    
    
    
    print ("this is a:")
    print(a)

    print ("this is b:")
    print(b)
    
    print ("this is x1:")
    print(x1)

    print ("this is x2:")
    print(x2)
  
    r1 = b - a.dot(x1)
    r2 = b - a.dot(x2)
   
    print ("this is |r1|_1:")
    print(np.linalg.norm(r1,1))

    
    print ("this is |r2|_1:")
    print(np.linalg.norm(r2,1))
          
          
# end of main()    
    
if __name__ == '__main__':
    main()
# end if
