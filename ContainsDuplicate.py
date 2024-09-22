def containsDuplicate(nums):
    seen = set() #container for numbers

    for num in nums: #iterate every function numbers
        if num in seen: #if numbers is already in container
            return True #if there is duplicates
        seen.add(num) #if not, add it to container

    return False #no duplicates

#test
print(containsDuplicate([1,1,2,3,4,5])) #expected result: True
print(containsDuplicate([1,3,6,7,8])) #expected result: False