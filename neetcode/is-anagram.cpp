#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int s_total = 0;
        unordered_map<char, int> s_map;

        for (int i = 0; i < s.size(); i++) {
            s_map[s[i]] += 1;
            s_total += 1;
        }

        for (int i = 0; i < t.size(); i++) {
            if (s_map[t[i]] <= 0) {
                return false;
            }
            s_map[t[i]] -= 1;
            s_total -= 1;
        }

        return s_total == 0;
    }
};

int main() {
    string s, t;
    Solution solution;

    s = "racecar", t = "carrace";
    cout << solution.isAnagram(s, t) << endl;

    s = "jar", t = "jam";
    cout << solution.isAnagram(s, t) << endl;

    s = "cross", t = "orcs";
    cout << solution.isAnagram(s, t) << endl;

    return 0;
}