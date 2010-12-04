import os
import tempfile

mytemp = tempfile.mkstemp()[1]

while True:  # adds indent
    with open(mytemp, 'wb') as file:
        print "Executing 'with' statement."
    break

os.unlink(mytemp)
