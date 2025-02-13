import csv

def save_to_csv(filename, data):
    """Save gRNA guides and mutation results to a CSV file."""

    with open(filename, "w", newline='') as csvfile: # Opens CSV file in writing mode. 
        csv_writer = csv.writer(csvfile) # Creates a CSV writer object. 

        # Writing the headers row: 
        csv_writer.writerow(["Guide Sequence", "Position", "#G in Window", "Mutation Type", "Original AA", "Mutated AA", "Mutated Positions"])
        
        # Loops through data and writes each entry (list) as a new row in the CSV file : 
        for row in data:
            csv_writer.writerow(row)
