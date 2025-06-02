def mergesort(my_list) :
    
    if len(my_list ) > 1 :
        
        mid = len(my_list) // 2
        left_side = my_list[:mid]
        right_side = my_list[mid:]
        
        mergesort(left_side)
        mergesort(right_side)
        
        i=j=k=0
        while i < len(left_side) and j < len(right_side) :
            if left_side[i] < right_side[j] :
                my_list[k] = left_side[i]
                i+=1
            else :
                my_list[k] = right_side[j]  
                
                j+=1
                
            k+=1
            
        while i < len(left_side)     :
            
            my_list[k] = left_side[i]
            i+=1
            k+=1
            
        while j < len (right_side) :
            my_list[k] = right_side[j]
            j+=1
            k+=1
            
            
my_list = [35,90,88,17,34,66,15,42,500,1000]

mergesort(my_list)
print(my_list)
               
                  
        
    
    
