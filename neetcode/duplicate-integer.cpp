#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> nums_map;
        for (int i = 0; i < nums.size(); i++)
        {
            nums_map[nums[i]]++;
            if (nums_map[nums[i]] > 1)
            {
                return true;
            }
        }
        return false;
    }
};

int main() {
    Solution s = Solution();

    vector<int> nums = {1, 2, 3, 3};
    cout << s.hasDuplicate(nums) << endl;

    nums = {1, 3, 2, 3};
    cout << s.hasDuplicate(nums) << endl;

    nums = {1, 2, 3};
    cout << s.hasDuplicate(nums) << endl;

    nums = {1, 2, 3, 4};
    cout << s.hasDuplicate(nums) << endl;

    return 0;
}
