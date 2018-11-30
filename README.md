# mtr-web

mtr-web is a WebSockets-based frontend for [mtr](http://www.bitwizard.nl/mtr/),
built with [Flask](http://flask.pocoo.org/) (Python),
[AngularJS](https://angularjs.org/),
and [angular-websocket](https://github.com/gdi2290/angular-websocket),
allowing you to ping/traceroute a network from a remote HTTP server. This is a
useful diagnostic tool while making changes to your own network configuration.

## Example

Works with ipv4+6!  
http://mtr.bambusmedia.de/ 

## Installation
https://github.com/blackjack4494/mtr-ext  

(NOTE! was built on Ubuntu18.04 - May not work everywhere!)  
There is a compiled version of mtr in this project included.

```sh
sudo apt-get install mtr python python-pip -y
git clone https://github.com/blackjack4494/mtr-web
cd mtr-web
pip install Flask-Sockets gunicorn
```

## Usage (client with integrated server)

```sh
gunicorn -b 0.0.0.0 -k flask_sockets.worker mtr-web:app
```

http://[your-ip]:8000

## Nginx reverse proxy

For easier usage set up an nginx reverse proxy
```
location / {
                proxy_pass http://localhost:8000/;
}
```
You can also bind it to a specific subdomain (e.g. mtr)

# Separate Client and Server

## Client

To set up a client-only use
```sh
gunicorn -b 0.0.0.0 -k flask_sockets.worker mtr-client-web:app
```

You can input your websocket source (needs mtr-srv)

## Server

To set up a server-only use
```
gunicorn -b 0.0.0.0:8070 -k flask_sockets.worker mtr-srv:app
```

You can now input the ip of your server with your running mtr-srv in the web client.
Right now you need to add the port [ip]:8070 to your ip.

# Run mtr-web as a 24/7 service

Right now you can easily use
```sh
screen
```

You just need to put it infront of the commands above.
