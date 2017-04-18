import os
import sys


def main(log_file, query_file):
    log_ips = set()
    with open(log_file) as f:
        for line in f:
            l = line.rstrip()
            if l:
                log_ips.add(l.split()[2])
    #print log_ips
    with open(query_file) as f:
        for line in f:
            l = line.rstrip()
            if l:
                if l in log_ips:
                    print 1
                else:
                    print 0


if __name__ == "__main__":
    # Check atleast 2 sys arg exists
    if len(sys.argv) < 3:
        sys.exit('Usage: python main.py log_file query_file')

    # Check whether log_file exists
    if not os.path.exists(sys.argv[1]):
        sys.exit('ERROR: File %s was not found!' % sys.argv[1])

    # Check whether query_file exists
    if not os.path.exists(sys.argv[2]):
        sys.exit('ERROR: File %s was not found!' % sys.argv[2])

    # Call main function
    main(sys.argv[1], sys.argv[2])

