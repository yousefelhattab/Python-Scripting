import smtplib
from email.mime.text import MIMEText
import socket

def send_email(subject, body, to_email):
    from_email = "linkvital20@gmail.com"
    password = "nwes rcsb evvf xiyo"  
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
        print("")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Please check your email and password.")
    except socket.gaierror:
        print("Failed to connect to the SMTP server. Please check your internet connection.")
    except smtplib.SMTPException as e:
        print(f"An error occurred while sending the email: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# Example usage
#if __name__ == "__main__":
   # send_email("Backup Completed", "The backup process has been completed successfully.", "linkvital20@gmail.com.com")

