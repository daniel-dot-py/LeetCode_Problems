def romanToiNT(s):
    list_of_data = []
    sum_values = []
    for i in s:
        list_of_data.append(i)
    #print(list_of_data)

    long = len(list_of_data)

    #M values
    for j in range(0,long):
        if list_of_data[j] == "M" and j == 0:
            sum_values.append(1000)
        elif list_of_data[j] == "M" and list_of_data[j-1] != "C":
            sum_values.append(1000)
        elif list_of_data[j] == "M" and list_of_data[j-1] == "C":
            sum_values.append(900)
        else:
            pass
    
    #D values
        if list_of_data[j] == "D" and j == 0:
            sum_values.append(500)
        elif list_of_data[j] == "D" and list_of_data[j-1] != "C":
            sum_values.append(500)
        elif list_of_data[j] == "D" and list_of_data[j-1] == "C":
            sum_values.append(400)
        else:
            pass

    #C values
        if list_of_data[j] == "C" and long == 1:
            sum_values.append(100)
        elif list_of_data[j] == "C" and j != long-1 and list_of_data[j+1] == "D":
            sum_values.append(0)
        elif list_of_data[j] == "C" and j != long-1 and list_of_data[j+1] == "M":
            sum_values.append(0)
        elif list_of_data[j] == "C" and j == 0 and list_of_data[j+1] != "M" and list_of_data[j+1] != "D":
            sum_values.append(100)
        elif list_of_data[j] == "C" and j != long-1 and list_of_data[j+1] != "M" and list_of_data[j+1] != "D" and list_of_data[j-1] != "X":
            sum_values.append(100)
        elif list_of_data[j] == "C" and list_of_data[j-1] == "X":
            sum_values.append(90)
        elif list_of_data[j] == "C" and j == long-1:
            sum_values.append(100)
        else:
            pass
    
    #L values
        if list_of_data[j] == "L" and j == 0:
                sum_values.append(50)
        elif list_of_data[j] == "L" and list_of_data[j-1] != "X":
                sum_values.append(50)
        elif list_of_data[j] == "L" and list_of_data[j-1] == "X":
                sum_values.append(40)
        else:
            pass
    
    #X values
        if list_of_data[j] == "X" and long == 1:
            sum_values.append(10)
        elif list_of_data[j] == "X" and j != long-1 and list_of_data[j+1] == "L":
            sum_values.append(0)
        elif list_of_data[j] == "X" and j != long-1 and list_of_data[j+1] == "C":
            sum_values.append(0)
        elif list_of_data[j] == "X" and j == 0 and list_of_data[j+1] != "C" and list_of_data[j+1] != "L":
            sum_values.append(10)
        elif list_of_data[j] == "X" and j != long-1 and list_of_data[j+1] != "C" and list_of_data[j+1] != "L" and list_of_data[j-1] != "I":
            sum_values.append(10)
        elif list_of_data[j] == "X" and list_of_data[j-1] == "I" and j != 0 :
            sum_values.append(9)
        elif list_of_data[j] == "X" and j == long-1:
            sum_values.append(10)
        else:
            pass
    
    #V values
        if list_of_data[j] == "V" and j == 0:
                sum_values.append(5)
        elif list_of_data[j] == "V" and list_of_data[j-1] != "I":
                sum_values.append(5)
        elif list_of_data[j] == "V" and list_of_data[j-1] == "I":
                sum_values.append(4)
        else:
            pass
    
    #I values
        if list_of_data[j] == "I" and j != long-1 and list_of_data[j+1] == "V":
            sum_values.append(0)
        elif list_of_data[j] == "I" and j != long-1 and list_of_data[j+1] == "X":
            sum_values.append(0)
        elif list_of_data[j] == "I" and j != long-1 and list_of_data[j+1] != "X" and list_of_data[j+1] != "V":
            sum_values.append(1)
        elif list_of_data[j] == "I":
            sum_values.append(1)
        else:
            pass
    
    return sum(sum_values)




s = "D"

result = romanToiNT(s)

print(result)
