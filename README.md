Email Automation with Voice is a Python-based project that enables users to send emails using voice commands. By integrating speech recognition and SMTP libraries, this tool helps automate email composition and delivery through simple spoken instructions—making it especially useful for accessibility, productivity, and hands-free usage.

Key Features:
Voice Recognition: Converts spoken words into text using the speech_recognition library.
Email Sending: Automates sending emails using Python’s built-in smtplib.
Dynamic Input: Capture recipient address, subject, and message via voice.
Confirmation: Asks for confirmation before sending the email.
Secure Authentication: Uses environment variables or input prompts to handle email credentials securely.

Technologies Used:
Python 3
speech_recognition for capturing voice input
smtplib for email sending
pyttsx3 for voice output (optional)
email.message for formatting email content
