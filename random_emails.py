import csv

# Function to read usernames from a file
def read_usernames_from_file(input_file="usernames.csv"):
    with open(input_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header
        usernames = [row[0] for row in reader]
    return usernames

# Function to generate emails from usernames
def generate_emails(usernames, domain="@aeroforcebase.com"):
    return [f"{username}{domain}" for username in usernames]

# Function to save emails to a new CSV file
def save_emails_to_csv(emails, output_file="emails.csv"):
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        # writer.writerow(["Email"])  # Header row
        writer.writerows([[email] for email in emails])  # Save each email as a row
    print(f"Emails saved to {output_file}.")

# Main execution
if __name__ == "__main__":
    # Step 1: Read usernames from the existing file
    usernames = read_usernames_from_file("random_usernames.txt")  # Replace with your actual usernames file

    # Step 2: Generate emails using the usernames
    domain = "@aeroforcebase.com"
    emails = generate_emails(usernames, domain)

    # Step 3: Save the generated emails to a new CSV file
    save_emails_to_csv(emails)

    print("Emails generated and saved successfully.")
