#! /usr/bin/python3
import pyperclip, re

phoneRegex= re.compile(r'\d\d\s\d\d\d\s\d\d\s\d\d')
phoneRegex1 = re.compile(r'\d\d\d\d\d\d\d\d\d')
phoneRegex2 = re.compile(r'\d\d-\d\d\d-\d\d-\d\d')
#phoneRegex= re.compile(r'''(
			#(\d){2}	# two first digits usually 78,77 or 76 
			#(\s|-|\.)?	# separators
			#(\d){3}	# three more digit 
			#(\s|-|\.)?	# separators 
			#(\d){2}	# 2 more digit  
			#(\s|-|\.)?	# separators
			#(\d){2}	# last two number
			#)''', re.VERBOSE)
# the mail regex 

mailRegex= re.compile(r'''(
			[a-zA-Z0-9._%+-]+
			@
			[a-zA-Z0-9.-]+
			\.[a-zA-Z]{2,4}
			)''', re.VERBOSE)
# find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	matches.append(groups)
for groups in phoneRegex1.findall(text):
	matches.append(groups)
for groups in phoneRegex2.findall(text):
	matches.append(groups)
for groups in mailRegex.findall(text):
	matches.append(groups)
if len(matches) > 0:
	mo = '\n'.join(matches)
	pyperclip.copy(mo)
	print('Copied to clipboard:')
	print(mo)
else:
	print('No phone numbers or email addresses found.')