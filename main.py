import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import schedule
import time
from threading import Thread
from backup import backup_files
from email_notification import send_email
from download_files import download_file
import os

class SchedulerGUI:
    def __init__(self, master):
        self.master = master
        master.title("NTI Project - File Download and Backup Scheduler")
        master.geometry("800x600")
        master.configure(bg="#F0F0F0")  # Light background color

        # Set custom style
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TFrame", background="#F0F0F0")
        self.style.configure("TLabel", font=("Roboto", 12), foreground="#333333", background="#F0F0F0")
        self.style.configure("TEntry", font=("Roboto", 12), fieldbackground="#FFFFFF", foreground="#000000")
        self.style.configure("TButton", font=("Roboto", 12), background="#4CAF50", foreground="#FFFFFF")
        self.style.map("TButton", background=[("active", "#45A049")])

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self.master, padding="20", style="TFrame")
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)

        # File URL
        ttk.Label(main_frame, text="File URL:").grid(row=0, column=0, sticky="e", padx=10, pady=10)
        self.file_url = self.create_entry(main_frame, 0)

        # Download Directory
        ttk.Label(main_frame, text="Download Directory:").grid(row=1, column=0, sticky="e", padx=10, pady=10)
        self.download_dir = self.create_directory_entry(main_frame, 1)

        # Backup Source
        ttk.Label(main_frame, text="Backup Source:").grid(row=2, column=0, sticky="e", padx=10, pady=10)
        self.backup_source = self.create_directory_entry(main_frame, 2)

        # Backup Destination
        ttk.Label(main_frame, text="Backup Destination:").grid(row=3, column=0, sticky="e", padx=10, pady=10)
        self.backup_dest = self.create_directory_entry(main_frame, 3)

        # Email Subject
        ttk.Label(main_frame, text="Email Subject:").grid(row=4, column=0, sticky="e", padx=10, pady=10)
        self.email_subject = self.create_entry(main_frame, 4)

        # Email Body
        ttk.Label(main_frame, text="Email Body:").grid(row=5, column=0, sticky="ne", padx=10, pady=10)
        self.email_body = self.create_text_area(main_frame, 5)

        # Email Recipient
        ttk.Label(main_frame, text="Email Recipient:").grid(row=6, column=0, sticky="e", padx=10, pady=10)
        self.email_recipient = self.create_entry(main_frame, 6)

        # Schedule Time
        ttk.Label(main_frame, text="Schedule Time (HH:MM):").grid(row=7, column=0, sticky="e", padx=10, pady=10)
        self.schedule_time = self.create_entry(main_frame, 7)

        # Schedule Button
        ttk.Button(main_frame, text="Schedule Job", command=self.schedule_job).grid(row=8, column=1, pady=20)

        for i in range(3):
            main_frame.grid_columnconfigure(i, weight=1)
        for i in range(9):
            main_frame.grid_rowconfigure(i, weight=1)

    def create_entry(self, frame, row):
        entry = ttk.Entry(frame, width=50, style="TEntry")
        entry.grid(row=row, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
        return entry

    def create_directory_entry(self, frame, row):
        entry = ttk.Entry(frame, width=50, style="TEntry")
        entry.grid(row=row, column=1, padx=5, pady=5, sticky="ew")
        ttk.Button(frame, text="Browse", command=lambda: self.browse_directory(entry)).grid(row=row, column=2, padx=5, pady=5)
        return entry

    def create_text_area(self, frame, row):
        text_area = tk.Text(frame, width=50, height=3, font=("Roboto", 10), bg="#FFFFFF", fg="#000000")
        text_area.grid(row=row, column=1, columnspan=2, padx=5, pady=5, sticky="ew")
        return text_area

    def browse_directory(self, entry):
        directory = filedialog.askdirectory()
        if directory:
            entry.delete(0, tk.END)
            entry.insert(0, directory)

    def schedule_job(self):
        file_url = self.file_url.get()
        download_directory = self.download_dir.get()
        backup_source = self.backup_source.get()
        backup_destination = self.backup_dest.get()
        email_subject = self.email_subject.get()
        email_body = self.email_body.get("1.0", tk.END).strip()
        email_recipient = self.email_recipient.get()
        schedule_time = self.schedule_time.get()

        if not all([file_url, download_directory, backup_source, backup_destination, 
                    email_subject, email_body, email_recipient, schedule_time]):
            messagebox.showerror("Error", "All fields are required!")
            return

        schedule.every().day.at(schedule_time).do(self.job, file_url, download_directory, 
                                                  backup_source, backup_destination, 
                                                  email_subject, email_body, email_recipient)

        messagebox.showinfo("Success", f"Job scheduled daily at {schedule_time}")
        
        # Start the scheduler in a separate thread
        Thread(target=self.run_scheduler, daemon=True).start()

    def job(self, file_url, download_directory, backup_source, backup_destination, 
            email_subject, email_body, email_recipient):
        if not os.path.exists(download_directory):
            os.makedirs(download_directory)

        try:
            download_file(file_url, download_directory)
            print("File downloaded successfully.")

            backup_files(backup_source, backup_destination)
            print("Backup completed successfully.")

            send_email(email_subject, email_body, email_recipient)
            print("Email sent successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")

    def run_scheduler(self):
        while True:
            schedule.run_pending()
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = SchedulerGUI(root)
    root.mainloop()
