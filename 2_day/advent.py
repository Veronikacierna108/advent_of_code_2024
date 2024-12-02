with open("input.txt","r", encoding= "utf-8") as file :
    rows = file.readlines()

#split rows 
splitet_rows = [row.split() for row in rows]

def check_list(alist):
    decreasing_counter = 0
    increasing_counter = 0
    difference_counter = 0

    for i in range(1,len(alist)):
        if int(alist[i]) < int(alist[i-1]):
            decreasing_counter += 1
        
        if int(alist[i]) > int(alist[i-1]):
             increasing_counter += 1

        if abs(int(alist[i]) - int(alist[i-1])) <= 3:
            difference_counter += 1      

    return (increasing_counter == difference_counter == (len(alist)) -1) or (decreasing_counter == difference_counter == (len(alist) -1))

def removing_level(alist):
    for i in range(len(alist)):
        new_list =  alist[:]
        new_list.pop(i)
        if check_list(new_list):
            return True
    return False

def check_safe_report(alist):
    counter = 0 
    for i in alist:
        if check_list(i):
            counter += 1
    return counter 

def check_safe_report2(alist):
    counter = 0 
    for i in alist:
        if removing_level(i):
            counter += 1
    return counter 

#first part 
print(check_safe_report(splitet_rows))

#second part 
#print(check_safe_report2(splitet_rows))
