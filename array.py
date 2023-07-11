import numpy as np
def main():
    a1 = np.ones((5,5),dtype=np.uint8)
    #print(a1.ndim)
    a2 = a1.copy() * 3
    #print(a2)
    a3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(a3)
    a4 = np.zeros((5,5),dtype=np.int8)
    #print(a4)
    a5 = np.array([1,2,4,3,8,1,0,2])
    #print(a5)
    slice1 = a5[2:5]
    #print(slice1)
    slice2 = a3[1:2,1:3]
    print(slice2)
    
if __name__ == '__main__':
    main()
    