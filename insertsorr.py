def insertion_sort (list_vals):                                                 
    num_of_elements = len(list_vals);                                           
    for i in range(0, num_of_elements):                                         
        # temp stores current element whose left side is traversed              
        # to find correct position                                              
        temp = list_vals[i];                                                    
        j = i;                                                                  
        # checks whether left side elements are less than current element.      
        while(j > 0 and temp < list_vals[j-1]):                                 
            list_vals[j] = list_vals[j-1];                                      
            j = j - 1;                                                          
                                                                                
        # moving current element to correct position in left side.              
        list_vals[j] = temp;                                                    
    return list_vals;                                                           
                                                                                
                                                                                
if __name__ == "__main__":                                                      
    list_vals = [30, 10, 20, 70, 60, 80, 50, 40];                               
    print("Collection before sorting: %s" % str(list_vals));                    
    print("Sorted list elements: %s" % str(insertion_sort(list_vals)));