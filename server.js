//var BinaryServer = require('../../../').BinaryServer;

var BinaryServer = require('binaryjs');
var fs = require('fs');
var express = require('express');
var app = express();

app.get('/', function(req, res) {
	res.sendfile("index.html");
});

var expressServer = app.listen(8000, function() {
	console.log("express is up and running on port 8000");
})

// Start Binary.js server
var server = BinaryServer.BinaryServer({port: 9000});
// Wait for new user connections
server.on('connection', function(client){
  // Stream a flower as a hello!
  var file = fs.createReadStream(__dirname + '/test3.json');
  client.send(file); 
});
