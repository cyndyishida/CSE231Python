# parameters mean, take something from the global namespace into the function's local namespace 
def shallow_example( list_1 = [1,2,3], list_2 = [] ):   # default values, means the user using my function can put in parameters, but if not these are the values 
    ''' example of how lists transfer from local to global namespace '''
    list_3 = list_2    # shallow copy list_3
    list_1.append(23)                       
    list_1.append(["cyndy"])          
    list_3.sort(reverse = True)       # set the "reverse" parameter to a value I want! 
    print("inside function: ",list_1, "\n")    
    return list_3                                  # bring list_3 from the local namespace into the global namespace by the return statement
     












t = int(input())
for i in range(t):
    n , summ = [int(i) for i in input().split()]
    combinations = [ int(i) for i in input().split()]
    dp = [0 for i in range(n! )]
    combinations.sort()
    for j in range(summ):
        for k in range(n):
            if combinations[k] > j:
                continue
            dp[j] = max(dp[j], combinations[k] + dp[j - combinations[k]])


    print(dp[summ])



























#include <bits/stdc++.h>
using namespace std;
vector <int> c; int dp[2005]; 
int main()
{
    int tc; cin >> tc;
    for (int g=0;g<tc; g++){c.clear(); memset(dp,0,sizeof(dp)); 
    int a,b; cin >> a >> b;
    for (int g=0;g<a; g++)
    {
    int d; cin >> d; c.push_back(d); 
    }sort(c.begin(), c.end());
    for (int g=1;g<=b; g++)
    {
        for (int y=0;y<c.size(); y++)
        {
            if (c[y]>g) continue;
            dp[g]=max(dp[g], c[y]+dp[g-c[y]]); 
        }
    }
    cout << dp[b] << '\n';} return 0; 
}









def main():
    first_list = [2,4,3] 
    third_list = shallow_example(first_list)     
    fourth_list = shallow_example()           # use the default value 
    
    print("First set of examples: ")
    print(first_list)
    print(third_list)
    print(fourth_list, "\n\n")    
    
    fourth_list = [100001, 0, 12]
    third_list = [34,54]
    fifth_list= shallow_example(third_list, fourth_list)


    print("Second set of examples: ")
    print(third_list)
    print(fourth_list)
    print(fifth_list)




main()