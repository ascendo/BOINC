"""
BASICS


MIDAS: Multiple Input Docker Automation System

Generates a github image with all user commands inside to be submitted to BOINC
"""

from flask import Flask, request, jsonify
import tarfile, shutil, os, sys
import preprocessing as pp
from werkzeug.utils import secure_filename
import redis


app = Flask(__name__)

# Basic operational check
@app.route("/boincserver/v2/midas_status")
def api_operational():
    return 'MIDAS APIs are active'

# MIDAS tutorial
# Tutorial
@app.route("/boincserver/v2/midas_tutorial")
def tutorial():
   
    full = {
    'Basics' : 'MIDAS (Multiple Input Docker Automation System) is a TACC developed tool ',
    'Disclaimer': 'API usage is restricted to users with granted access, Token required. To test token, curl ->\
                  http://{BOINC_IP}:5000/boincserver/test_token=ENTER_TOKEN',
    'User guide': {'Steps': 'Submit a tar.gz file containing a compressed folder with all the files. File must be a tar.gz , all other inputs will not be accepted .',
                   'Contents' : 'All files must contain a README.txt (file ending MUST be .txt, all other inputs will not be accepted',
                   'README.txt': 'Follow instructions, curl -> http://SERVER_IP/boincserver/README_MIDAS_example.txt',

                   'Other files': 'Their number and name must be accounted for in the README',
                   'Outputs': 'Their full path must be included'            

                  },
                  
    'Limitations': 'MIDAS is based on Docker publicly available Docker images. As such, only open-source, free to use software is allowed. No Intel compilers, software that requires key access, enterprise editions, or private OS (Windows, Mac are not allowed)'
    'Supported Languages': {'Current': 'None',
                            'Short Term Future Updates':'Python, Go, Bash scripts (Short Term)',
                            'Long Term Future Updates':'Haskell, OCaml, C, C++'
                           },
    'Supported OS': {'Current':'Ubuntu 16.04'},

    'Root Access': 'Assume root access when installing dependencies trough a bash script'

    }

    return jsonify(full)

# Allows the user to see how much space is still available in his allocation
# Allows to check the user's allocation status
@app.route('/boincserver/v2/midas_allocation_status/token=<toktok>')
def reef_allocation_status(toktok):
    if pp.token_test(toktok) == False:
       return 'Invalid token'
    used_space = pp.user_sandbox_size(str(toktok))/1073741824
    assigned_allocation = r.get(toktok).decode('UTF-8')
    all_info = {'Max. allocation': assigned_allocation+' GB',
                'Used space': str(used_space)+' GB', 
                'Space available left': str((1 - used_space/float(assigned_allocation))*100)+'% allocation available'}

    return jsonify(all_info)


if __name__ == '__main__':
   app.run(host ='0.0.0.0', port = 5085)
