from collections import deque,Counter
from bisect import insort, bisect_left
from itertools import islice

def RunningMode(seq,N,M):
    """
    Purpose: Find the mode for the points in a sliding window as it 
             is moved from left (beginning of seq) to right (end of seq)
             by one point at a time.
     Inputs:
          seq -- list containing items for which a running mode (in a sliding window) is 
                 to be calculated
            N -- length of sequence                      
            M -- number of items in window (window size) -- must be an integer > 1
     Otputs:
        modes -- list of modes with size M - N + 1
       Note:
         1. The mode is the value that appears most often in a set of data.
         2. In the case of ties it the last of the ties that is taken as the mode (this
            is not by definition).
    """    
    # Load deque with first window of seq 
    d = deque(seq[0:M]) 

    modes = [Counter(d).most_common(1)[0][0]]  # contains mode of first window

    # Now slide the window by one point to the right for each new position (each pass through 
    # the loop). Stop when the item in the right end of the deque contains the last item in seq
    for item in islice(seq,M,N):
        old = d.popleft()                      # pop oldest from left
        d.append(item)                         # push newest in from right
        modes.append(Counter(d).most_common(1)[0][0])        
    return modes    

def RunningMedian(seq, M):
    """
     Purpose: Find the median for the points in a sliding window (odd number in size) 
              as it is moved from left to right by one point at a time.
      Inputs:
            seq -- list containing items for which a running median (in a sliding window) 
                   is to be calculated
              M -- number of items in window (window size) -- must be an integer > 1
      Otputs:
         medians -- list of medians with size N - M + 1
       Note:
         1. The median of a finite list of numbers is the "center" value when this list
            is sorted in ascending order. 
         2. If M is an even number the two elements in the window that
            are close to the center are averaged to give the median (this
            is not by definition)
    """   
    seq = iter(seq)
    s = []   
    m = M // 2

    # Set up list s (to be sorted) and load deque with first window of seq
    s = [item for item in islice(seq,M)]    
    d = deque(s)

    # Simple lambda function to handle even/odd window sizes    
    median = lambda : s[m] if bool(M&1) else (s[m-1]+s[m])*0.5

    # Sort it in increasing order and extract the median ("center" of the sorted window)
    s.sort()    
    medians = [median()]   

    # Now slide the window by one point to the right for each new position (each pass through 
    # the loop). Stop when the item in the right end of the deque contains the last item in seq
    for item in seq:
        old = d.popleft()          # pop oldest from left
        d.append(item)             # push newest in from right
        del s[bisect_left(s, old)] # locate insertion point and then remove old 
        insort(s, item)            # insert newest such that new sort is not required        
        medians.append(median())  
    return medians

def RunningMean(seq,N,M):
    """
     Purpose: Find the mean for the points in a sliding window (fixed size) 
              as it is moved from left to right by one point at a time.
      Inputs:
          seq -- list containing items for which a mean (in a sliding window) is 
                 to be calculated (N items)
            N -- length of sequence     
            M -- number of items in sliding window
      Otputs:
        means -- list of means with size N - M + 1    

    """    
    # Load deque (d) with first window of seq
    d = deque(seq[0:M])
    means = [float(sum(d))/len(d)] # contains mean of first window
    # Now slide the window by one point to the right for each new position (each pass through 
    # the loop). Stop when the item in the right end of the deque contains the last item in seq
    for item in islice(seq,M,N):
        old = d.popleft()            # pop oldest from left
        d.append(item)               # push newest in from right
        m = float(sum(d))/len(d)
        means.append(m)     # mean for current window
    return means  

#*** Start of test area *****************************************************
#
# Set random seed for repeatability
yn = [3,2,-1.0,2.0,3.0,5.0,-5.0,6.0,-5.0,4.0,9.0,6.3,1.3,0.0,-7.0,1.3,-5.0]
#yn = [3,2,-1.0,-1.0,-1.0,5.0,5.0]
#yn = [5,5.0,5,5.0,5]
#yn = [3,3,3,3,3,3,3]
#yn = [3.,3.,3.,3.,3.,3.,3.]
#yn = [-1,1,-1,1,-1,1]
#yn = [3,2,-1.0,2.0]
#yn = [5,3,2,2,-1]
#yn = [-5.0,3.0,2.0,2.0,-1.0]

N = len(yn)

# Try the follwing window sizes
#M = 1
#M = 2
M = 3
#M = 4
#M = 5
#M = 6
if M <= N and M >= 1:
    print 'M = %2d,'%M,
    print 'yn:'
    print yn

    means = RunningMean(yn,N,M)
    print ' Means(%d):' %(N-M+1)
    print means

    medians = RunningMedian(yn,M)
    print ' Medians(%d):' %(N-M+1)
    print medians

    modes = RunningMode(yn,N,M)
    print ' Modes(%d):' %(N-M+1)
    print modes
else:
    print 'Window size (M=%d) out of range'%M
