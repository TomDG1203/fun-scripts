import random
import sys
import smtplib

# Check if there are enough command line arguments
if len(sys.argv) < 2:
  print('Usage: secret_santa.py email_1 email_2 email_3 ...')
  sys.exit(1)

# The list of participants in the secret santa exchange
participants = sys.argv[1:]

# Shuffle the list of participants randomly
random.shuffle(participants)

# Create a dictionary to store the secret santa assignments
assignments = {}

# Iterate through the list of participants, assigning each person
# as the secret santa for the next person in the list
for i in range(len(participants)):
  assignments[participants[i]] = participants[(i+1) % len(participants)]

# Set up the SMTP server
server = smtplib.SMTP('smtp.example.com')

# Send an email to each participant with their secret santa assignment
for person, secret_santa in assignments.items():
  message = f'You are the secret santa for {secret_santa}'
  server.sendmail('secretsanta@example.com', person, message)

# Close the SMTP server
server.quit()