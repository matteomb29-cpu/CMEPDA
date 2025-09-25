import multiprocessing 

def square_list(mylist, result, square_sum): 

    for idx, num in enumerate(mylist):  #enumerate prende una lista e la trasforma in una 
        #serie numerata cioè crea anche la lista degli indici associata alla lista che
        #passi a enumerate
        
        result[idx] = num * num  


    # square_sum value dove questa variabile square_sum è una istanza della classe 
    #multiprocessing.Value
    square_sum.value = sum(result) 

    # print result Array 
    print("Result(in process p1): "+str(result[:])) 
    # print square_sum Value 
    print("Sum of squares(in process p1): "+str(square_sum.value)) 

if __name__== "__main__":    
    # input list 
    mylist = [1,2,3,4] 


    # creating Array of int data type with space for 4 integers 
    result = multiprocessing.Array('i', 4) 

    #la libraria multiprocessing possiede anche l' oggetto Array, Value oltre
    #al già incontrato Process

    # creating Value of int data type 
    square_sum = multiprocessing.Value('i')  

    #esiste una classe chiamata multiprocessing.Value che ha come attributo value
    #per questo utilizzo square_sum.valore()


    # creating new process 
    p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum)) 
    
    # starting process 
    p1.start() 
    # wait until process is finished 
    p1.join() 
    
    # print result array 
    print("Result(in main program): "+str(result[:])) 
    # print square_sum Value 
    print("Sum of squares(in main program): "+str(square_sum.value)) 
    

