#i made quite diff sol just to use test matplotlib and visualise
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.axes_divider import make_axes_area_auto_adjustable


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_area = 0
        #adding some extra variables
        max_left = left
        max_right = right


        while left < right:
            width = right - left
            current_height = min(height[left],height[right])
            current_area = current_height * width

            if current_area > max_area:
                max_area = current_area
                max_left = left
                max_right = right

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area, max_left, max_right

#test
solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
max_area, max_left, max_right = solution.maxArea(height)
print(f"Maximum capacity: {max_area}")
print(f"Position: {max_left} and {max_right}")

positions = np.arange(len(height))

plt.figure(figsize=(12, 6))
plt.bar(positions, height, color='lightblue', edgecolor='black')
plt.bar([max_left, max_right], [height[max_left], height[max_right]], color='lightgreen', edgecolor='black')

x_fill = [max_left, max_left, max_right, max_right]
y_fill = [0, min(height[max_left], height[max_right]), min(height[max_left], height[max_right]), 0]
plt.fill_between(x_fill, y_fill, color='lightgreen', alpha=0.3)

plt.title('Container With Most Water')
plt.xlabel('Position')
plt.ylabel('Height')
plt.xticks(positions)
plt.legend(['Bars', 'Max container'])

plt.show()
