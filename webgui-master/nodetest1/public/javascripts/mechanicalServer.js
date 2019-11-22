var socket = io('http://192.168.87.66:3000');
  socket.on('hello', function( type, number) {
    switch(type) {
      case 'battery' : {
        document.getElementById('bt-num').innerHTML = number + "°";
          number/=90;
          number*=100;
          $("#battery").css("width", number + "%");
          $("#battery").attr("aria-valuenow", number);
        break;
      }
      case 'voltage' : {
        document.getElementById('bv-num').innerHTML = number + "v";
        number/=10;
          $("#voltage").css("width", number + "%");
          $("#voltage").attr("aria-valuenow", number);
        break;
      }
      case 'temp' : {
        document.getElementById('ct-num').innerHTML = number + "°";
          number/=90;
          number*=100;
          $("#colant").css("width", number + "%");
          $("#colant").attr("aria-valuenow", number);
        break;
      }
      case 'wheelfront' : {
        document.getElementById('ws-front').innerHTML = number + "km/h";
        $("#front").css("width", number + "%");
        $("#front").attr("aria-valuenow", number);
      }
      case 'wheelrear' : {
        document.getElementById('ws-rear').innerHTML = number + "km/h";
        $("#rear").css("width", number + "%");
        $("#rear").attr("aria-valuenow", number);
      }

      default: break;
    }

});
