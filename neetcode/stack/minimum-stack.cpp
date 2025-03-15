#include <iostream>
#include <stack>

using namespace std;

class MinStack {
public:
    stack<int> st = {}, stMin = {};

    void push(int val) {
        int min = val;
        if (stMin.size() > 0 && stMin.top() < min) {
            min = stMin.top();
        }

        st.push(val);
        stMin.push(min);
    }

    void pop() {
        st.pop();
        stMin.pop();
    }

    int top() {
        return st.top();
    }

    int getMin() {
        return stMin.top();;
    }
};

int main() {
    // MinStack minStack;
    // minStack.push(1);
    // minStack.push(2);
    // minStack.push(0);
    // cout << minStack.getMin() << endl; // return 0
    // minStack.pop();
    // cout << minStack.top()    << endl; // return 2
    // cout << minStack.getMin() << endl; // return 1

    // cout << endl;

    MinStack minStack;
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    cout << minStack.getMin() << endl; // -3
    minStack.pop();
    cout << minStack.top() << endl;    // 0
    cout << minStack.getMin() << endl; // -2
    minStack.push(2);
    minStack.push(-4);
    minStack.push(3);
    cout << minStack.getMin() << endl; // -4
    minStack.pop();
    cout << minStack.getMin() << endl; // -4
    minStack.pop();
    cout << minStack.top() << endl;    // 2
    cout << minStack.getMin() << endl; // 0 RETORNAND -3
    minStack.pop();
    cout << minStack.top() << endl;    // 0
    cout << minStack.getMin() << endl; // -2
    return 0;
}