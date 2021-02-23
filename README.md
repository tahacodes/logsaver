# logsaver-api

using flask, and mariadb

development:
    pip install flask
    pip install pymongo

how to use:
    save your logs on the client like this (as a text file):
        <status>,<timestamp>,<response>
    some examples are provided in 'sample-logs' file.

    now you can POST this file:
        curl http://<server_ip>:<port> \                                                      
            -H "Content-type: multipart/form-data" \
            -F file=@<logs_file_location>
