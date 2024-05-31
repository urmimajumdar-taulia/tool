import re

def parse_log_file(input_file, output_file):
    # Define the regex pattern for matching timestamp and error messages
    timestamp_pattern = re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    error_pattern = re.compile(r'ERROR')
    
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            if error_pattern.search(line):
                timestamp_match = timestamp_pattern.search(line)
                if timestamp_match:
                    outfile.write(line)

if __name__ == "__main__":
    input_file = 'sample_log.log'
    output_file = 'error_log.txt'
    parse_log_file(input_file, output_file)
    print(f'Errors have been written to {output_file}')

