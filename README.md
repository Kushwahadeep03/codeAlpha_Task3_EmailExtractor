# codeAlpha_Task3_EmailExtractor

## Overview
This Python script automates the task of extracting all email addresses from a text file and saving them into a new file.  
It is a small real-life automation task using Python.

## Key Concepts Used
- *Python Modules:* re (regular expressions)
- *File Handling:* Reading and writing files

## How It Works
1. The script reads a text file named input.txt.
2. It uses a regular expression to find all email addresses in the text.
3. All extracted emails are saved into a new file named emails.txt.

## How to Run
1. Make sure you have Python installed on your system.
2. Place your input text file input.txt in the same folder as the script.
3. Open a terminal in VS Code and run the script:

```bash
python Task3_EmailExtractor.py

4. After running, check the folder for the emails.txt file containing all extracted emails.



Example

input.txt

Hello my email is deep@gmail.com and my other email is test@yahoo.com.
Contact us at support@website.com.

emails.txt (after running the script)

deep@gmail.com
test@yahoo.com
support@website.com
