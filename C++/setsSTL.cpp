#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    vector<int> arr;

    cin >> n;

    for (int i=0; i<n; i++)
    {
        int type;
        cin >> type;

        switch (type) 
        {
            case 1: // add
            {
                int num;
                cin >> num;
                arr.push_back(num);
                break;
            }
            
            case 2: // delete
            {
                int del;
                cin >> del;
                for (int i = 0; i < arr.size(); i++)
                {
                    if (del == arr[i])
                    {
                        arr.erase(arr.begin() + i);
                    }
                }
                break;
            }

            case 3: // search
            {
                bool found = false;
                int search;
                cin >> search;
                for (int i = 0; i < arr.size(); i++)
                {
                    if (search == arr[i])
                    {
                        found = true;
                    }
                }

                if (found == true)
                {
                    cout << "Yes" << endl;
                }
                else
                {
                    cout << "No" << endl;
                }

                break;
            }
        }
    }

    return 0;
}

// or

int main() {
int iCount;
set<int> ss;
cin >> iCount;
for (int i=0; i<iCount; ++i){
    int type, query;
    cin >> type >> query;
    switch (type){
        case 1:
            ss.insert(query);
            break;
        case 2:
            ss.erase(query);
            break;
        case 3:
            cout << (ss.find(query) == ss.end() ? "No" : "Yes") << endl;
            break;
    }
}  
return 0;
}

