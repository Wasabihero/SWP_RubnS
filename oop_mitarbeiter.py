list = [1,2,3,4,5]
def filtermethod():
     if (x % 2 == 0):
         return True
     else:
         return False
     list(filter(filtermethod(), list))
