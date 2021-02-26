# logsaver-api

using flask, and mongodb
<br>
<hr />
<br>

# development: 
    pip install flask # a microservice web framework<br>
    pip install pymongo # mongodb driver

# how to use:
    save your logs on the client like this (as a text file):
        "(OK|ERR),timestamp,response"
    some examples are provided in 'sample-logs' file.

    now you can POST this file:
        curl http://<server_ip>:<port> \                                                      
            -H "Content-type: multipart/form-data" \
            -F file=@<logs_file_location>
