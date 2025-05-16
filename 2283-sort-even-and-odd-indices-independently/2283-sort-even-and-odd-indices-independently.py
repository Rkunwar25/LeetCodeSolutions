class Solution(object):
    def sortEvenOdd(self, nums):
        # l1=[nums[i] for i in range(len(nums)) if i%2==0]
        # l2=[nums[i] for i in range(len(nums)) if i%2!=0]
        # l1.sort()
        # l2.sort(reverse=True)
        # l=[]
        # k1=0
        # k2=0
        # for i in range(len(l1)+len(l2)):
        #     if i%2==0:          
        #         l.append(l1[k1])
        #         k1+=1
        #     else:
        #         l.append(l2[k2])
        #         k2+=1
        # return l
        even = nums[::2]
        odd = nums[1::2]

        even.sort()
        odd.sort(reverse=True)
        
        nums[::2] = even
        nums[1::2] = odd
        
        return nums