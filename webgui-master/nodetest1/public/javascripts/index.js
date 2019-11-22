var app = require('express')();

/*Get HOME page*/
app.get('/', function(req, res) {
    res.sendFile( __dirname + '/index.html');
});

/* GET mechanical page. */
app.get('/mechanical', function(req, res) {
    res.sendFile( __dirname + '/mechanical.html');
});

/* GET electrical page. */
app.get('/electrical', function(req, res) {
  res.sendFile( __dirname + '/electrical.html');

});

/* GET start up page. */
app.get('/start-up', function(req, res) {
  res.sendFile( __dirname + '/start-up.html');
});

/*GET competition page*/
app.get('/comp', function(req, res) {
  res.sendFile( __dirname + '/comp.html');
});

/*GET log page*/
app.get('/log', function(req, res) {
  res.sendFile( __dirname + '/log.html');
});

/*GET Sign in page*/
app.get('/sign-in', function(req, res) {
  res.sendFile( __dirname + '/sign-in.html');
});
module.exports = app;
