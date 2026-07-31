"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


height=[1,8,6,2,5,4,8,3,7]
# height=[1,1]
def brutal_force(height):
    max_area=0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            area=(j-1) * min(height[i],height[j])
            max_area=max(max_area,area)
    print(max_area)
    
# brutal_force(height)


def optimized(height):
        left_p=0
        right=len(height)-1
        max_area=0
        while left_p < right:
            h_left = height[left_p]
            h_right = height[right]

            h = h_left if h_left < h_right else h_right
            area = h * (right - left_p)
            
            if area > max_area:
                max_area=area
            if height[left_p] < height[right]:
                left_p+=1
            else:
                right-=1
        return max_area

print(optimized(height))
         