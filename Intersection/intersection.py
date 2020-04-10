'''
	This problem was recently asked by Amazon:
	
	Given 2 Arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays

	Note:
	Each element in the result must be unique.
	The result can be in any order

	EXAMPLE 1:
	Input: nums1 = [1,2,2,1], nums2 = [2,2]
	Output: [2]

	Example 2:
	Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
	Output: [9,4]
'''


class Intersection:
	def intersection(self, nums1, nums2):
		# Initialize an empty array that will store our common numbers
		commons = []
		# Verifies whether an element at a current index of an array is present at any index in another array
		for i in range (len(nums2)):
			for j in range (len(nums1)):
				if nums2[i] == nums1[j]:
					commons.append(nums1[j])
		# create a list dictionary out of the array of common digits to remove all duplicates
		commons = list(dict.fromkeys(commons))
		return commons
		
# print(Intersection().intersection([4,9,5],[9,4,9,8,4]))
# print(Intersection().intersection([1,2,2,1],[2,2]))
