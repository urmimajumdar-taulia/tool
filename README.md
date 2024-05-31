# tool
Various tools in python for DevOps and iSRE troubleshooting
log_error_parser.py: The script opens the input log file for reading and the output file for writing.
It iterates through each line of the input file, checks for the "ERROR" keyword, and ensures the line contains a timestamp.
If both conditions are met, the line is written to the output file.
