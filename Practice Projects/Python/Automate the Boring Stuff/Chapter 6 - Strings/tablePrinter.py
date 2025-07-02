"""This program takes a list of lists of strings and organizes
them into a well organized table with each column right-just
ified."""

tableData = [['apples', 'oranges', 'cherries', 'banana'], 
             ['Alice', 'Bob', 'Carol', 'David'], 
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(lists):
    #create a empty list that will be filled with the 
    #maximum width of each list.
    
    listLen = len(tableData[0]) #length of a list
    
    colWidths = [0] * len(lists) #list that stores the width of each column

    #we need to find the maximum width in each list first:
    #iterate through each list:
    for i in range(len(lists)):
        maxLen = 0
        
        """For the j'th string in the i'th list..."""
        for j in range(listLen):
            if len(lists[i][j]) > maxLen:
                maxLen = len(lists[i][j])

        colWidths[i] = maxLen

    #create a new list to hold justified lists
    justLists = []
    
    #fill justlists with empty lists
    for i in range(len(lists)):
        justLists.append([0]*listLen)

    #now iterate through justlists to insert the new string
    #values
    for i in range(len(lists)):
        for j in range(0,listLen):
            #sets the j'th string in the i'th list to 
            #a right-justified version of the original string
            justLists[i][j] = lists[i][j].rjust(colWidths[i])

    #now use another nested loop to print the strings in 
    #each loop
    
    #for the i'th row along all 3 lists...
    for i in range(listLen):
        
        for j in range(len(lists)):
            #print the item in the j'th column.
            #for example, if i = 0, the order goes:
            #list 0 -> item 0, list 1 -> item 0, and list 2 -> item 0.
            #and they're all printed on the same line with the 'end' keyword.
            print(justLists[j][i]+" ",end = '') 

        #newline for the next row of items
        print()

printTable(tableData)

        
       
    
