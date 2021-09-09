"""Generate sales report showing total melons each salesperson sold."""
#--------------------
#open the sales report file
f = open('sales-report.txt')

melon_dict = {}

for line in f:#for each line in the file, split it up by |
    line = line.rstrip()
    entries = line.split('|')#now we have a list called entries for each line in the text file
    
    for i in range(len(entries)-2):#populate the dictionary with names as keys
        key= entries[0]
        melon_dict[key] = melon_dict.get(key, []) 
        melon_dict[key].append(float(entries[1]))
        melon_dict[key].append(int(entries[2]))
       
for name, value in melon_dict.items():
    total_cost = sum(value[0::2])
    total_count = sum(value[1::2])
    print(name.upper()) #prints name in uppercase
    print(f'sold ${total_cost}: {total_count} melons')
    print("====================")


#-------------------------------
#make empty lists for salespeople and melons sold
# salespeople = []
# melons_sold = []    
# salesperson = entries[0]#assign the 0th item to salesperson
#     melons = int(entries[2])#assign the int value of the 2nd item to melons

#     if salesperson in salespeople:#if the salesperson is already in salespeople list
#         position = salespeople.index(salesperson)#assign position to the index of salesperson in salespeople

#         melons_sold[position] += melons#add the int value of melons to the melons sold list to the person at their index
#     else:
#         salespeople.append(salesperson)#otherwise, add the salesperson to the salespeople list
#         melons_sold.append(melons)#and add the melons value to the melons sold list

# for i in range(len(salespeople)):#iterate through the salespeople list
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')#and print out how many melons each person sold

