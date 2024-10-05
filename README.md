# NTI
project:

Key functionalities of the code:**

* File Download: Downloads a specified file to a designated directory.
* File Backup: Backs up files from a source directory to a destination directory.
* Email Notification: Sends an email notification with a specified subject and body.
* Scheduling: Allows users to schedule the above tasks to run daily at a specific time.

Steps involved:

1. User Input: Users enter details like file URL, download directory, backup source/destination, email information, and schedule time.
2. Scheduling: The entered information is used to create a scheduled job that will run daily at the specified time.
3. Task Execution: When the scheduled time arrives, the job is executed:
   - The file is downloaded.
   - Files are backed up.
   - An email notification is sent.
4. Error Handling: The code includes error handling to catch and display any exceptions that may occur during the process.

GUI Interface:

* A graphical user interface (GUI) is created using Tkinter.
* The GUI allows users to enter the necessary information and schedule the tasks.
* Buttons are provided for browsing directories and scheduling the job.



# GUI Creation:
Creates a main window with the title "File Download and Backup Scheduler".
Uses various widgets (Label, Entry, Button, Text) to create an interface for user input and interaction.
Connects buttons to their respective functions (browse_directory and schedule_job).
Starts the main event loop (mainloop) to display the GUI and respond to user actions.
Overall, this code provides a user-friendly interface for scheduling automated tasks involving file downloads, backups, and email notifications.
