function autoRefreshPage(){ window.location = href.location; }
$(document).ready(function socket(){

  $(body).css('visibility', 'hidden');
  if(localStorage.getItem('loggedIn') != 1) {
    alert('You need to be logged in to access this page');
    window.location = '/sign-in'
  } else {
    $(body).css('visibility', 'visible');
  }

  var socket = io('http://192.168.87.66:3000'); //Connects to the library transferring data from the server to html
  //Listening to a line essentiallyu

  socket.on('speed', function(number) {
    console.log(number);
    $('#sc-value').html(number + "km/h");
    number/=200;
    number*=100;
    $("#speedometer").css("width", number + "%");
    $("#speedometer").attr("aria-valuenow", number);
  });

socket.on('throttle', function(number) {
  $('#steer-num').html(number + "°");
  number/=1000;
  number*=100;
  $("#dynamic").css("width", number + "%");
  $("#dynamic").attr("aria-valuenow", number);
});

//     socket.on('hello', function( type, number) {
//       switch(type) {
//         case 'brake' : {
//           //document.getElementById('brake-value').innerHTML = number+"%";
//           $('#brake-value').html(number + "%");
//           $("#brake").css("width", number + "%");
//           $("#brake").attr("aria-valuenow", number);
//           break;
//         }
//         case 'bms' : $('#bms-number').html(number);break;
//         case 'voltage' : {
//           //document.getElementById('vol-value').innerHTML = number + "v";
//           $('#vol-value').html(number + "v");
//           number/=10;
//           $("#voltage").css("width", number + "%");
//           $("#voltage").attr("aria-valuenow", number);
//           break;
//         }
//         case 'temp' : {
//           //document.getElementById('temp-value').innerHTML = number + "°c";
//           $('#temp-value').html(number + "°c");
//           number/=90;
//           number*=100;
//           $("#temperature").css("width", number + "%");
//           $("#temperature").attr("aria-valuenow", number);
//           break;
//         }
//         case 'df-fault1' : document.getElementById('df-fault-1').style.backgroundColor = "#dc0000"; break;
//         case 'df-fault2' : document.getElementById('df-fault-2').style.backgroundColor = "#dc0000"; break;
//         case 'df-fault3' : document.getElementById('df-fault-3').style.backgroundColor = "#dc0000"; break;
//         case 'df-fault4' : document.getElementById('df-fault-4').style.backgroundColor = "#dc0000"; break;
//         case 'fault1' : document.getElementById('fault-1').style.backgroundColor = "#dc0000"; break;
//         case 'fault2' : document.getElementById('df-fault-2').style.backgroundColor = "#dc0000"; break;
//         case 'fault3' : document.getElementById('df-fault-3').style.backgroundColor = "#dc0000"; break;
//         case 'fault4' : document.getElementById('df-fault-4').style.backgroundColor = "#dc0000"; break;
//         case 'battery' : {
//             // document.getElementById('bt-num').innerHTML = number + "°";
//             $('#bt-num').html(number + "°c");
//             number/=90;
//             number*=100;
//             $("#battery").css("width", number + "%");
//             $("#battery").attr("aria-valuenow", number);
//           break;
//         }
//         case 'batvol' : {
//           // document.getElementById('bv-num').innerHTML = number + "v";
//           $('#bv-num').html(number + "v");
//           number/=10;
//             $("#batvol").css("width", number + "%");
//             $("#batvol").attr("aria-valuenow", number);
//           break;
//         }
//         case 'coolant' : {
//           // document.getElementById('ct-num').innerHTML = number + "°";
//           $('#ct-num').html( number + "°c");
//             $("#colant").css("width", number + "%");
//             $("#colant").attr("aria-valuenow", number);
//           break;
//         }
//         case 'wheelfront' : {
//           // document.getElementById('ws-front').innerHTML = number + "km/h";
//           $('#ws-front').html(number + "km/h");
//           $("#front").css("width", number + "%");
//           $("#front").attr("aria-valuenow", number);
//         }
//         case 'wheelrear' : {
//           //document.getElementById('ws-rear').innerHTML = number + "km/h";
//           $('#ws-rear').html(number + "km/h");
//           $("#rear").css("width", number + "%");
//           $("#rear").attr("aria-valuenow", number);
//         }
//         default: break;
//       }
//
//
//
//   });

});
