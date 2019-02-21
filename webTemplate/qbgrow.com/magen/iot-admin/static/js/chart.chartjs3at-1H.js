$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartat1H').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
      labels: ['00', '03', '06', '09', '12', '15','18','21','24','27','30','33','36','39','32','35','38','41','44','47','50','53','56','59'],
      datasets: [{
        data: [12, 39, 20, 10, 25, 18,25,23,11,1,36,12,23,6,24,15,32,12, 39, 20, 10, 25, 18, 10, 25, 18, ],
        borderColor: 'red',
        label: '# Votes ',
        backgroundColor: '#FFDFDF'

      }]
    },
    options: {
      legend: {
        display: false,
          labels: {
            display: false
          }
      },
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 10,
            max: 80
          }, gridLines:{
            display:false}
        }],
        xAxes: [{
          ticks: {
            beginAtZero:true,
            fontSize: 11
          }, gridLines:{
            display:false}
        }]
      }
    }
  });
});
