  def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
      stack1 = []
      next_greater_element_dict = {}
      for i in nums2:
          if not stack1 or stack1[-1] > i:
              stack1.append(i)
              continue


          while stack1 and stack1[-1] < i:
              next_greater_element_dict[stack1.pop()] = i
          stack1.append(i)
      result_list = []
      for i in nums1:
          try:
              result_list.append(next_greater_element_dict[i])
          except:
              result_list.append(-1)
      return result_list
