
var usernames = ['j.emanouel@utsmotorsports.com', 's.emanouel@utsmotorsports.com']
var passwords = ['1234', '1234']



function submit() {

  var username = document.getElementById("exampleInputEmail1").value;
  var password = document.getElementById("exampleInputPassword1").value;

    // var socket = io('http://localhost:3000');
    // socket.emit('login', username, password);
    // socket.on('userFound', function(answer) {
    //   if(answer === 'yes') {
    //     window.location = '/'
    //     console.log("yes")
    //   } else {
    //     alert('Wrong username and/or password.')
    //   }
    // });


  for(i = 0; i < usernames.length; i++) {
    if(usernames[i] === username) {
      if(passwords[i] === password) {
        alert("Welcome");
        localStorage.setItem('loggedIn', '1');
        window.location = '/';
        break;
      }
      if(usernames[i] != username && passwords[i] != password || usernames[i] != username || passwords[i] != password) {
        alert("Wrong username and/or password");
        return;
      } 
      break;
    }

    if(usernames[i] != username && passwords[i] != password || usernames[i] != username || passwords[i] != password) {
      alert("Wrong username and/or password");
      return;
    }
  }
}
