# mtr-web

mtr-web is a WebSockets-based frontend for [mtr](http://www.bitwizard.nl/mtr/),
built with [Flask](http://flask.pocoo.org/) (Python),
[AngularJS](https://angularjs.org/),
and [angular-websocket](https://github.com/gdi2290/angular-websocket),
allowing you to ping/traceroute a network from a remote HTTP server. This is a
useful diagnostic tool while making changes to your own network configuration.

## Example

http://103.68.109.131:8000/

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

## Usage

```sh
gunicorn -b 0.0.0.0 -k flask_sockets.worker mtr-web:app
```

http://[your-ip]:8000
