App used - DVWA(Damn vulnerable web application)
Port 80
Method - Docker

step
1.Installed docker 

sudo apt install docker.io

2.start docker

sudo systemctl start docker
sudo systemctl enable docker

3.run dvwa using docker

sudo docker run --rm -it -p 80:80 vulnerables/web-dvwa

4.open browser

http://localhost
