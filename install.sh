sudo cp catflapmagnet.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable catflapmagnet
sudo systemctl start catflapmagnet