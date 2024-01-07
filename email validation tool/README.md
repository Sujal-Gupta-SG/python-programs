# Email Validation Tool

## Overview
The Email Validation Tool is a Python project designed to verify the accuracy and validity of email addresses. This tool ensures that email addresses entered by users meet specific criteria commonly associated with valid email addresses. It's a valuable resource for individuals and organizations looking to enhance data accuracy and reduce errors in email-related processes.

## Key Features
- **Length Requirement:** The tool checks if the email address provided is at least 6 characters long, a standard requirement for most valid email addresses.

- **Alphabetic First Character:** It verifies that the email address starts with an alphabetic character, in accordance with email address conventions.

- **Single '@' Symbol:** The tool ensures that there is exactly one "@" symbol in the email address, adhering to email address standards.

- **Proper Domain Extension:** It checks for a valid domain extension (e.g., ".com," ".org") by examining the last three or four characters of the email address.

- **Character Validation:** The tool examines each character in the email address and checks for any invalid characters, such as spaces or special characters other than "_", ".", and "@".

- **Case Sensitivity:** It detects if there are uppercase characters in the email address, as emails are case-insensitive.

## Usage
1. Clone this repository to your local machine.
2. Run the Python script.
3. Enter an email address when prompted.
4. The tool will validate the email address based on the specified criteria.
5. You will receive a validation result, indicating whether the email address is valid or not.

## Example
Here's an example of how to use the Email Validation Tool:
```shell
$ python Email_Validation_Tool.py
Enter your Email : user@example.com
Email Validated
