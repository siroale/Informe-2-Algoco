deleteCost = "2"
insertCost = "1"
categories = ["insert", "delete", "replace", "transpose"]


def fillRow (file, cost):
    row = ""
    for i in range(26):
        row += cost + " " 
    
    file.write(row)
    return


def fillSustChart (file):
    size = 26
    for a in range(size):
        row = ""
        for b in range(size):
            if a == b:
                row += "0 "     
                continue
            
            if abs(a - b) <= (size/2):
                row += str(abs(a - b)) + " " 

            else:
                row += str(size - abs(a-b)) + " "
        
        row = row[:len(row)] + "\n"
        file.write(row)

    return



for fileType in categories:
    file = open("cost_" + fileType + ".txt", "w")
    
    if fileType == "delete":
        fillRow(file, deleteCost)
    
    elif fileType == "insert":
        fillRow(file, insertCost)

    elif fileType == "replace":
        fillSustChart(file)
    
    elif fileType == "transpose":
        fillSustChart(file)

    file.close()