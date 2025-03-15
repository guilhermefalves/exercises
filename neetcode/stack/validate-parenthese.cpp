#include <stack>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

class Solution {
public:
    unordered_map<char, char> closeChars = {
        {')', '('}, {']', '['}, {'}', '{'},
    };

    bool isValid(string s) {
        if (s.size() % 2 != 0) {
            return false;
        }

        stack<char> st;
        for (char c : s) {
            if (isOpenChar(c)) {
                st.push(c);
                continue;
            }

            if (st.size() > 0 && st.top() == closeChars[c]) {
                st.pop();
                continue;
            }

            return false;
        }

        return st.size() == 0;
    }

    bool isOpenChar(char c) {
        return c == '(' || c == '[' || c == '{';
    }
};

int main () {
    Solution s;
    string str;

    str = "()";
    cout << s.isValid(str) << endl;

    str = "([])";
    cout << s.isValid(str) << endl;

    str = "([)]";
    cout << s.isValid(str) << endl;

    str = "]]";
    cout << s.isValid(str) << endl;
    str = "(])(])";
    cout << s.isValid(str) << endl;

    return 0;
}