import shutil
import os

def backup_files(source, backup_folder):
    shutil.make_archive(backup_folder, 'zip', source)
    print(f"Backup completed: {backup_folder}.zip")


#backup_files('D:\Project', 'D:\Backup')
