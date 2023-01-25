def nextPermutation(self, nums: List[int]) -> None:
        def reverse(i,j):
            while(i<j):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j-=1
        i=len(nums)-2
        while(i>=0 and nums[i]>=nums[i+1]):
            i-=1
        if(i>=0):
            j=len(nums)-1
            while(j>=0 and nums[i]>=nums[j]):
                j-=1
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp
        reverse(i+1,len(nums)-1)
        
