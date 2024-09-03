# Redact-No-Console
 This is a revised version of my redaction script. 
 The goal of this simple program is redact IP addresses within a log in the even the logs will be shown to others or the general public.
 Another goal is have error handling in preventing directory traversal when choosing your file. The user will set the aboslute path within
 the code and when prompt to select the file, the user will only be able to choose a file within the designated folder.
 After the file has been choosen, two more prompts will ask for IP address 1 and 2, the user can add or take away whatever is needed.
 Once the addresses are choosen the program will redacted those address and give you the option to save the file.
