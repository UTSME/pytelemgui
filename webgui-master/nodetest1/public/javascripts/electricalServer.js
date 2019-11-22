var socket = io('http://192.168.87.66:3000');


  socket.on('speed', function(number) {
    console.log("Speed: " + number);
    addData(myChart, 7, number);
  });


    socket.on('throttle', function(number) {
      console.log("Throttle: " + number);
      addBarData(myChart2, 7, number);
    });

// socket.on('hello', function( type, number) {
// switch(type) {
//   case 'Speed' : {
//     var data = document.getElementById('data').innerHTML
//     data = number + "°";
//     var min =   myChart.data.datasets[0];
//     var max =   myChart.data.datasets[2];
//     if(data < min) { min.data.push(number);}
//     if(data > max) { max.data.push(number); }
//     break;
//   }
//   case 'Speed' : {
//     addBarData(myChart2, 0, number);
//     break;
//   }
//   case 'speed' : {
//     addData(myChart, 7, number);
//     break;
//   }
//   default: break;
// }
// });

function addData(chart, label, data) {
  chart.data.labels.push(label);
  chart.data.datasets.forEach((dataset) => {
    dataset.data.push(data);
    // if(dataset.data.length > 100) {
    //   chart.data.labels.shift();
    //   dataset.data[0] = dataset.data[1];
    //   dataset.data.splice(1, 1);
    // }
  });
  chart.update();
}

function addBarData(chart, label, data) {
  chart.data.labels.push(label);
  chart.data.labels.shift();
  chart.data.datasets.forEach((dataset) => {
    dataset.data.push(data);
    dataset.data[0] = dataset.data[1];
    dataset.data.splice(1, 1);
  });
  chart.update();
}

function removeData(chart) {
  chart.data.labels.pop();
  dataset.data.pop();
  chart.update();
}


var ctx = document.getElementById('line-chart').getContext("2d");
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      datasets: [{
        label: 'Speed',
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)'
          ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)'
          ],
          borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true,
                    suggestedMax: 100
                }
            }]
        }, xAxes: [{
          ticks: {
            maxTicksLimit: 10
          }
        }]
    }
});

var ctx2 = document.getElementById('bar-chart').getContext("2d");
var myChart2 = new Chart(ctx2, {
    type: 'bar',
    data: {
        datasets: [{
            label: 'BMS Min',
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }, {
            label: 'BMS Current',
            backgroundColor: [
              'rgba(73, 162, 204, 0.2)',
              'rgba(54, 162, 235, 0.2)',
              'rgba(73, 162, 204, 0.2)',
              'rgba(75, 192, 192, 0.2)',
              'rgba(153, 102, 255, 0.2)',
              'rgba(73, 162, 204, 0.2)'
            ],
            borderColor: [
              'rgba(73, 162, 204, 1)',
              'rgba(54, 162, 235, 1)',
              'rgba(73, 162, 204, 1)',
              'rgba(75, 192, 192, 1)',
              'rgba(153, 102, 255, 1)',
              'rgba(73, 162, 204, 1)'
            ],
            borderWidth: 1
        }, {
            label: 'BMS Max',
            backgroundColor: [
                'rgba(73, 204, 115, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(73, 204, 115, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(73, 204, 115, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(73, 204, 115, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(73, 204, 115, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(73, 204, 115, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                  autoSkip: true,
                  beginAtZero: true,
                  suggestedMax: 100
                }
            }]
        }
    }
});
