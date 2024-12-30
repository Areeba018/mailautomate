import csv

def create_extended_csv(input_file="processed.csv", output_file="stocktwits_accounts.csv"):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            
            # Check if 'Processed' column exists
            if "Processed" not in reader.fieldnames:
                raise ValueError("The 'Processed' column is missing in the input CSV file.")
            
            # Add new fields
            fieldnames = reader.fieldnames + ["Stocktwits Username", "Stocktwits Password"]

            rows = []
            for row in reader:
                processed_status = row.get("Processed")
                
                # Safely handle missing or empty 'Processed' field
                if processed_status and processed_status.strip().lower() == "yes":
                    # Populate Stocktwits fields
                    row["Stocktwits Username"] = row.get("Email", "")
                    row["Stocktwits Password"] = row.get("Password", "")
                else:
                    # Leave Stocktwits fields empty for non-processed rows
                    row["Stocktwits Username"] = ""
                    row["Stocktwits Password"] = ""
                
                rows.append(row)

        # Write to the new CSV file
        with open(output_file, 'w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"File '{output_file}' created successfully with Stocktwits fields populated for processed rows.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function to create the new file
# create_extended_csv()
