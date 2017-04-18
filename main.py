import os
import sys


def main(log_file, query_file):
    # Initialize log_ips set
    log_ips = set()

    try:
        # Open log_file
        with open(log_file) as f:
            # Read line by line
            for line in f:
                # Strip whitespaces and blank lines
                l = line.rstrip()
                if l:
                    # Add ip address to set
                    log_ips.add(l.split()[2])
    except Exception as e:
        print "Error occurred %s" % str(e)

    #print log_ips

    try:
        # Open query_file
        with open(query_file) as f:
            # Read line by line
            for line in f:
                # Strip whitespaces and blank lines
                l = line.rstrip()
                if l:
                    # Check ip is in set
                    if l in log_ips:
                        print 1
                    else:
                        print 0
    except Exception as e:
        print "Error occurred %s" % str(e)


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

