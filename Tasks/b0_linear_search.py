"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""


	minItem = arr[0]
	minIndex = 0
	for i in range(len(arr)):
		if arr[i] < minItem:
			minItem = arr[i]
			minIndex = i


	return minIndex

