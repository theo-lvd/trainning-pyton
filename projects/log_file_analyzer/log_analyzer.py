import os


#TOOLS :

def analyze_log_file(filename):
    error_lines = []
    with open(filename, "r") as sample_log :
        log_raw = sample_log.read()
        log_lines = log_raw.split("\n")

        for lines in log_lines :
            if "ERROR" in lines :
                error_lines.append(lines)
        return error_lines


def write_error_report(filename, error_lines) :
    with open(filename, "w") as error_report_log :
        for lines in error_lines :
            error_report_log.write(lines + "\n")


#MAIN SCRIPT :
script_dir = os.path.dirname(__file__) 

log_file = os.path.join(script_dir, "sample.log")
error_report_file = os.path.join(script_dir, "error_report.log")

report = analyze_log_file(log_file)
write_error_report(error_report_file, report)

print("Report generated successfuly.")
