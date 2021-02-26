# logsaver-api

using flask, and mongodb
<br>

# development: 
    pip install flask # a microservice web framework
    pip install pymongo # mongodb driver

# how to use:
    save your logs on the client like this (as a text file):
        "(OK|ERR),timestamp,response"
    some examples are provided in 'sample-logs' file.

    now you can POST this file:
        curl http://<server_ip>:<port> \                                                      
            -H "Content-type: multipart/form-data" \
            -F file=@<logs_file_location>

# server configs

nginx config: /etc/nginx/sites-available/reverse-proxy.conf

    server {
        listen 80;
        listen [::]:80;

        access_log /var/log/nginx/reverse-access.log;
        error_log /var/log/nginx/reverse-error.log;

        location /first {
                return 200 "It's alright";
                add_header Content-Type text/plain;
        }

        location /second {
                return 418 "I'm a teapot";
                add_header Content-Type text/plain;
        }

        location / {
                include uwsgi_params;
                uwsgi_pass unix:/home/<user>/logsaver/logsaver.sock;
        }
    }

and then:

    sudo ln -s /etc/nginx/sites-available/reverse-proxy.conf /etc/nginx/sites-enabled/reverse-proxy.conf
    sudo nginx -t #test nginx configurations before restarting it
    sudo systemctl restart nginx

<br>
systemd service: /etc/systemd/system/logsaver.service

    [Unit]
    Description=uWSGI instance to serve logsaver
    After=network.target mongod.service

    [Service]
    User=<user>
    Group=www-data
    WorkingDirectory=/home/<user>/logsaver
    Environment="PATH=/home/<user>/logsaver/venv/bin"
    ExecStart=/home/<user>/logsaver/venv/bin/uwsgi --ini logsaver.ini

    [Install]
    WantedBy=multi-user.target

and then:

    sudo systemctl enable logsaver
    sudo systemctl start logsaver
