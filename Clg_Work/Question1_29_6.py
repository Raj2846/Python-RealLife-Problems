# index accessing directly like array 

rollnum=['A']*30
search=int(input("Enter the roll number to search"))
rollnum[search-1]='P'
print(rollnum)