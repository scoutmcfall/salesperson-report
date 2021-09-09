"""Generate sales report showing total melons each salesperson sold."""

#make empty lists for salespeople and melons sold
salespeople = []
melons_sold = []
#open the sales report file
f = open('sales-report.txt')
for line in f:#for each line in the file, split it up by |
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0]#assign the 0th item to salesperson
    melons = int(entries[2])#assign the int value of the 2nd item to melons

    if salesperson in salespeople:#if the salesperson is already in salespeople list
        position = salespeople.index(salesperson)#assign position to the index of salesperson in salespeople

        melons_sold[position] += melons#add the int value of melons to the melons sold list to the person at their index
    else:
        salespeople.append(salesperson)#otherwise, add the salesperson to the salespeople list
        melons_sold.append(melons)#and add the melons value to the melons sold list


for i in range(len(salespeople)):#iterate through the salespeople list
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')#and print out how many melons each person sold
