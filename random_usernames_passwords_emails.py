import csv

def combine_usernames_passwords_emails(usernames_file, passwords_file, output_file, domain="@aeroforcebase.com"):
    """
    Combines usernames, passwords, and emails row by row from two files
    and saves them to a CSV file.
    """
    with open(usernames_file, 'r') as u_file, open(passwords_file, 'r') as p_file, open(output_file, 'w', newline='') as out_file:
        # Read usernames and passwords
        usernames = u_file.readlines()
        passwords = p_file.readlines()

        # Ensure both files have the same number of rows
        if len(usernames) != len(passwords):
            raise ValueError("The number of usernames and passwords must be equal.")

        # Write to CSV
        csv_writer = csv.writer(out_file)
        csv_writer.writerow(["Username", "Email", "Password"])  # Header row

        for username, password in zip(usernames, passwords):
            username = username.strip()
            password = password.strip()
            email = f"{username}{domain}"  # Generate email
            csv_writer.writerow([username, email, password])

    print(f"Usernames, emails, and passwords have been combined and saved to '{output_file}'.")

# File paths
usernames_file = "random_usernames.txt"  # Replace with your username file path
passwords_file = "random_passwords.txt"  # Replace with your password file path
output_file = "username_email_password_pairs.csv"  # Output CSV file

# Call the function
combine_usernames_passwords_emails(usernames_file, passwords_file, output_file)
