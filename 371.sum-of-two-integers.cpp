/*
 * @lc app=leetcode id=371 lang=cpp
 *
 * [371] Sum of Two Integers
 */

// @lc code=start
class Solution
{
public:
    int getSum(int a, int b)
    {
        while (b != 0)
        {
            a = a ^ b;
            b = a & b << 1;
        }
        return a ^ b;
    }
};
// @lc code=end
