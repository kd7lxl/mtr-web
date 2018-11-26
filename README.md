# mtr-web

mtr-web is a WebSockets-based frontend for [mtr](http://www.bitwizard.nl/mtr/),
built with [Flask](http://flask.pocoo.org/) (Python),
[AngularJS](https://angularjs.org/),
and [angular-websocket](https://github.com/gdi2290/angular-websocket),
allowing you to ping/traceroute a network from a remote HTTP server. This is a
useful diagnostic tool while making changes to your own network configuration.

## Example

~~http://trace.hamwan.net/~~

## Installation

```sh
sudo apt-get install mtr python python-pip
git clone https://github.com/blackjack4494/mtr-web
cd mtr-web
pip install Flask-Sockets gunicorn
```

## Usage

```sh
gunicorn -b 0.0.0.0 -k flask_sockets.worker mtr-web:app
```

http://127.0.0.1:8000

## Proxy through nginx

```nginx
server {
        listen 80;
        listen [::]:80;
        server_name trace.hamwan.net;

        location / {
                proxy_pass http://127.0.0.1:8000;
        }

        location /mtr {
                proxy_pass http://127.0.0.1:8000;
                proxy_http_version 1.1;
                proxy_set_header Upgrade $http_upgrade;
                proxy_set_header Connection "upgrade";
        }
}
```
