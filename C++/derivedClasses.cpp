#include <iostream>

using namespace std;
/*
 * Create classes Rectangle and RectangleArea
 */
class Rectangle 
{
protected:
    int l;
    int w;
public:
    virtual void display() const
    {
        cout << l << " " << w << endl;
    }
};

class RectangleArea : public Rectangle
{
public:
    void read_input()
    {
        cin >> l >> w;
    }

    void display() const override
    {
        cout << l*w << endl;
    }
};


