# Strange Number :--
import math
'''
def checkFactors(n):
    count = 0
    i = 2
    while i <= n:
        if n % i == 0:
            count+=1
            n//=i
            i-=1
        i+=1
    return count
'''
def checkFactors(n): 
    count = 0
    while n % 2 == 0: 
        count +=1
        n = n / 2
          
    for i in range(3, int(math.sqrt(n))+1, 2): 
        while n % i == 0: 
            count +=1 
            n = n / i 
              
    if n > 2: 
        count +=1
    return count

for _ in range(int(input())):
    x,k = map(int,input().split())
    if checkFactors(x) >= k :
        print(1)
    else:
        print(0)
    
'''

void primefactor(int a){
    while(a%2==0){
        cout<<"2*";
        a/=2;

    for(int i=3; i<=sqrt(a); i+=2){
        while(a%i==0){
            cout<<i<<"*";
            a=a/i;
        }
    }
    if(a>2){
        cout<<a<<endl;
    }

}

'''
