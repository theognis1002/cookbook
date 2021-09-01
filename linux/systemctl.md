***Example service file: `/etc/systemd/system/<service_name>.service`***

[Unit]
Description=my_app
After=network.target
StartLimitIntervalSec=30
StartLimitBurst=5

[Service]
Type=simple
User=johndoe
Group=johndoe
WorkingDirectory=/johndoe/my_app
ExecStart=/usr/bin/bash -c "/johndoe/my_app/venv/bin/python run.py"
Environment=PYTHONUNBUFFERED=1
Restart=always
RestartSec=60

[Install]
WantedBy=multi-user.target


*** Steps to setting up systemctl ***
1. create `.service` file in `/etc/systemd/system/`
1. `systemctl daemon-reload`
    - reload so system registers new service file changes
1. `systemctl start <service_name>`
    - check out that everything is working
1. `systemctl enable`
    - starts service on boot
1. `journalctl -u <service_name>` -f
    - check tail of service logs
