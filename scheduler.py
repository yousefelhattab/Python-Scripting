import schedule
import time
from backup import backup_files
from email_notification import send_email
from download_files import download_file
import os

def job(file_url, download_directory, backup_source, backup_destination, email_subject, email_body, email_recipient):
    # Ensure the download directory exists
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    try:
        # Download the file
        download_file(file_url, download_directory)
        print("File downloaded successfully.")

        # Backup files
        backup_files(backup_source, backup_destination)
        print("Backup completed successfully.")

        # Send email notification
        send_email(email_subject, email_body, email_recipient)
        print("Email sent successfully.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Get input from the user
file_url = input("Enter the file URL to download: ")
download_directory = input("Enter the download directory path: ")
backup_source = input("Enter the source directory for backup: ")
backup_destination = input("Enter the destination directory for backup: ")
email_subject = input("Enter the email subject: ")
email_body = input("Enter the email body: ")
email_recipient = input("Enter the recipient email address: ")
schedule_time = input("Enter the time to schedule the job (in 24-hour format, e.g., 14:30): ")

# Schedule the job with user inputs
schedule.every().day.at(schedule_time).do(job, file_url, download_directory, backup_source, backup_destination, email_subject, email_body, email_recipient)

print(f"Job scheduled daily at {schedule_time}")

# Infinite loop to run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
