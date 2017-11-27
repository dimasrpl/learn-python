def swap(list_vals, min_val_index, i):                                          
    temp = list_vals[min_val_index];                                            
    list_vals[min_val_index] = list_vals[i];                                    
    list_vals[i] = temp;                                                        
                                                                                
def selection_sort(list_vals):                                                  
    num_of_elements = len(list_vals);                                           
                                                                                
    #  reduces the each inner iteration loop size by one.                       
    for i in range(0, num_of_elements-1):                                       
        # position of minimum element in the list                               
        # Assuming first element to be the minimum                              
        min_val_index = i;                                                      
        # finds minimum value position in the list of elements.                 
        for j in range(i+1, num_of_elements):                                   
            if (list_vals[j] < list_vals[min_val_index]):                       
                min_val_index = j;                                              
                                                                                
        swap(list_vals, min_val_index, i);                                      
                                                                                
    return list_vals;                                                           
                                                                                
if __name__ == "__main__":                                                      
    list_vals = [30, 10, 20, 70, 60, 80, 50, 40];                               
    print("Collection before sorting: %s" % str(list_vals));                    
    print("Sorted list elements: %s" % str(selection_sort(list_vals)));  

"""
def selectionSort(sample):
 print("sample=",sample)
 
 for i in range(len(sample)):
  print(sample)
  j = i+1
  minIndex = i
  while (j < len(sample)):
   if (sample[j] < sample[minIndex]):
    minIndex = j
   j+=1
  sample[i], sample[minIndex] = sample[minIndex], sample[i]
 
 print(sample)

sample1 = [12,77,88,34,22,66,474,21]
selectionSort(sample1)
"""