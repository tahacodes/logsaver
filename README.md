# logsaver-api

using flask, and mariadb
<br>
<hr />
<br>
development: <br>
    pip install flask # a microservice web framework<br>
    pip install pymongo # mongodb driver

how to use:<br>
    save your logs on the client like this (as a text file):<br>
        "status,timestamp,response"<br>
    some examples are provided in 'sample-logs' file.

    now you can POST this file:
        curl http://<server_ip>:<port> \                                                      
            -H "Content-type: multipart/form-data" \
            -F file=@<logs_file_location>
