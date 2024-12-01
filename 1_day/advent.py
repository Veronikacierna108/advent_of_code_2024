with open("input.txt","r", encoding= "utf-8") as file :
    rows = file.readlines()

#split rows 
splitet_rows = [row.split() for row in rows]

first_part = [int(row[0]) for row  in splitet_rows]
second_part = [int(row[1]) for row in splitet_rows]

#ordering
first_part.sort()
second_part.sort()

#fist part od problem 
def find_distance(list1,list2):
    result = 0 
    for i in range(len(list1)):
        result += abs(list1[i]- list2[i])
    print(result)




#second part of problem
def similalirity(list1,list2):
    parcial_result = {}
    result = 0
    for i in list1:
        for j in list2:
            if i == j:
                parcial_result[i] = parcial_result.get(j,0) + 1
    
    keys = list(parcial_result.keys())
    values = list(parcial_result.values())
    for i in  range(len(keys)):
        result += keys[i]* values[i]
    print(result) 



#slovnik = similalirity(first_part,second_part)
#keys = list(slovnik.keys())
#values = list(slovnik.values())



#results
find_distance(first_part,second_part)
similalirity(first_part,second_part)
