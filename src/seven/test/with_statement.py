import os
import tempfile

mytemp = tempfile.mkstemp()[1]

with open(mytemp, 'wb') as file:
    print "Executing 'with' statement."

os.unlink(mytemp)
