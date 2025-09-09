/*
 * @lc app=leetcode id=42 lang=c
 *
 * [42] Trapping Rain Water
 */

// @lc code=start
int trap(int *height, int heightSize)
{
    int water = 0;
    int l = 0;
    int r = heightSize - 1;
    int maxL = 0;
    int maxR = 0;
    while (l < r)
    {
        if (height[l] < height[r])
        {
            if (height[l] >= maxL)
            {
                maxL = height[l];
            }
            else
            {
                water += maxL - height[l];
            }
            l++;
        }
        else
        {
            if (height[r] >= maxR)
            {
                maxR = height[r];
            }
            else
            {
                water += maxR - height[r];
            }
            r--;
        }
    }
    return water;
}
// @lc code=end
