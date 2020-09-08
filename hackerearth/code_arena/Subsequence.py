# sub Secquence

def test(s):
    acount = 0
    bcount = 0
    ccount = 0
    
    for i in range(len(s)):
        if s[i] == 'a':
            acount = (1+2*acount)
        
        elif s[i] == 'b':
            bcount = (acount + 2*bcount)
        
        elif s[i] == 'c':
            ccount = (bcount +2*ccount)
            
    return ccount
        

# Write your code here
s = input()
count = test(s)
print(count)

'''
def test(s): 
  
    aCount = 0
  
    bCount = 0
  
    cCount = 0
  
    for i in range(len(s)): 

        if (s[i] == 'a'): 
            aCount = (1 + 2 * aCount) 
  
        elif (s[i] == 'b'): 
            bCount = (aCount + 2 * bCount) 

        elif (s[i] == 'c'): 
            cCount = (bCount + 2 * cCount) 
  
    return cCount 
  
# Driver code 
if __name__ == "__main__": 
    s = "abcabc"
    print(test(s))
'''

