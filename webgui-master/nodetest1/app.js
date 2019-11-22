var createError = require('http-errors');
var express = require('express');
var path = require('path');

var cookieParser = require('cookie-parser');
// var logger = require('morgan');
const app = express();

const PORT = process.env.PORT || 3000; //The port the server is listening to, this should stay the same
const server = app.listen(PORT);
var io = require('socket.io')(server);
var socket = io.listen(server);
var indexRouter = require('./public/javascripts/index.js');
app.use(express.static(__dirname + '/public'));

app.use('/', indexRouter);
app.io = socket;
/***********************************DONT CHANGE ANYTHING ABOVE THIS LINE **********************************************************/

var db = 'mongodb://localhost:27020'; //The database, change this to the pi's database
var MongoClient = require('mongodb').MongoClient;

// Connect to the db
function database() {
  MongoClient.connect(db, { useNewUrlParser: true }, function (err, db) {
    if(err) {
      throw err;
    } else {
      var db = db.db('UTSM19-2019-11-16'); //The database in mongodb
      var speedCollection = db.collection("Speed"); //The collection in mongodb

      const changeSpeedStream = speedCollection.watch();

      changeSpeedStream.on("change", function(event) {
        console.log("Speed: " + event.fullDocument.Speed);
        io.emit('speed', JSON.stringify(event.fullDocument.Speed));
      });

      var throttleCollection = db.collection("Throttle");
      const changeThrottleStream = throttleCollection.watch();
      changeThrottleStream.on("change", function(event) {
        console.log("Throttle: " + event.fullDocument.ThrottleLow);
        io.emit('throttle', JSON.stringify(event.fullDocument.ThrottleLow));
      });

      var bmsCollection = db.collection("BMS Main");
      const changeBMSStream = bmsCollection.watch();
      changeBMSStream.on("change", function(event) {
        console.log("BMS: " + event.fullDocument.bmsmain);
        io.emit('throttle', JSON.stringify(event.fullDocument.bmsmain));
      });


      io.on('login', function(err, username1, password1) {
        if(err) throw err;
        var userCollection = db.collection('users');
        userCollection.findOne({username: username1, password: password1}, function(err, doc) {
          if(err) throw err;
          if(doc) {
            socket.emit('userFound', 'yes');
            console.log("FOUND");
          } else {
               socket.emit("userFound", 'yes');
               console.log("NO")
             }
        });
      })
      // var userCollection = db.collection('users');
      // userCollection.findOne({username: "jasmine", password: "1234"}, function(err, doc) {
      //   if(err) throw err;
      //   if(doc) {
      //     console.log("FOUND");
      //     socket.emit('userFound', 'yes');
      //   } else {
      //     socket.emit("userFound", 'no');
      //     console.log("NO")
      //   }
      // })

    }
  });
}
database();

// setInterval(database, 500);
/***********************************DONT CHANGE ANYTHING BELOW THIS LINE **********************************************************/

// view engine setup
app.set('views', path.join(__dirname, 'public/views'));
app.set('view engine', 'ejs');

// app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

// Make our db accessible to our router
app.use(function(req,res,next){
  req.db = db;
  next();
});



// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
// set locals, only providing error in development
res.locals.message = err.message;
res.locals.error = req.app.get('env') === 'development' ? err : {};

// render the error page
res.status(err.status || 500);
res.render('error.ejs');
});

module.exports = app;
// module.exports.io = io;
