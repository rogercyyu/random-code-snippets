#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <map>
#include <algorithm>
#include <string>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int n;
    cin >> n;

    map <string, int> m;

    for (int i=0; i<n; i++)
    {
        int type;
        int grade;
        string name;

        cin >> type >> name;

        switch(type){
            case 1: // add
            {
                cin >> grade;
                m.insert(make_pair(name, m[name]+=grade));
                break;
            }
            case 2: // erase
            {
                m.erase(name);

                break;
            }
            case 3: // show
            {
                map<string,int>::iterator itr=m.find(name);
                if (itr!=m.end())
                {
                    cout << itr->second << endl;
                }
                else 
                {
                    cout << "0" << endl;
                }
                
                break;
            }

            
        }
        
    }

    return 0;
}



