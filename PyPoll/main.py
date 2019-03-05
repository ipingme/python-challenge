import os
import csv

total_votes = 0
candidate_list = []
candidate_dictionary = {}

# Open the CSV
file = os.path.join("Resources", "election_data.csv")

with open(file, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header
    header = next(csvreader)  

    # Loop through each row
    for row in csvreader:
        # totals number of votes and creates list of candidates
        total_votes += 1
        name = str(row[2])
        # Condition to add candidates to dictionary with total votes
        if name not in candidate_list:
            # Adding a new key value pair
            candidate_dictionary[name] = 1
            # Adds candidate name to candidate_list
            candidate_list.append(row[3-1])
        else:
            # Adds 1 to each candidates vote total
            candidate_dictionary[name] += 1

    # print(candidate_dictionary)

    # The percentage and total of votes each candidate won
    khan_percentage = (candidate_dictionary["Khan"] / total_votes) * 100
    khan_total = candidate_dictionary["Khan"]
    correy_percentage = (candidate_dictionary["Correy"] / total_votes) * 100
    correy_total = candidate_dictionary["Correy"]
    li_percentage = (candidate_dictionary["Li"] / total_votes) * 100
    li_total = candidate_dictionary["Li"]
    otooley_percentage = (candidate_dictionary["O'Tooley"] / total_votes) * 100
    otooley_total = candidate_dictionary["O'Tooley"]
    
    # Finds the winner who has the max votes
    max_key = max(candidate_dictionary, key=lambda k: candidate_dictionary[k])
    # print(max_key)

    # Prints all the results
    print(f"Election Results")
    print(f"----------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------")
    print(f"Khan: {khan_percentage:.3f}% ({khan_total})")
    print(f"Correy: {correy_percentage:.3f}% ({correy_total})")
    print(f"Li: {li_percentage:.3f}% ({li_total})")
    print(f"O'Tooley: {otooley_percentage:.3f}% ({otooley_total})")
    print(f"----------------------------")
    print(f"Winner: {max_key}")
    print(f"----------------------------")
    
    # Specify the file to write to
    output_path = os.path.join("Resources", "PyPoll_Summary.txt")

    # Open the file using "write" mode.
    with open(output_path, 'w') as text_file:
        text_file.write(f"Election Results")
        text_file.write(f"\n----------------------------")
        text_file.write(f"\nTotal Votes: {total_votes}")
        text_file.write(f"\n----------------------------")
        text_file.write(f"\nKhan: {khan_percentage:.3f}% ({khan_total})")
        text_file.write(f"\nCorrey: {correy_percentage:.3f}% ({correy_total})")
        text_file.write(f"\nLi: {li_percentage:.3f}% ({li_total})")
        text_file.write(f"\nO'Tooley: {otooley_percentage:.3f}% ({otooley_total})")
        text_file.write(f"\n----------------------------")
        text_file.write(f"\nWinner: {max_key}")
        text_file.write(f"\n----------------------------")
        text_file.close()