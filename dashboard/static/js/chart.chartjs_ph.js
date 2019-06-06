$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartsm1H').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
      labels: time,
      datasets: [{
        data: ph,
        borderColor: '#40E0D0',
        label: 'pH',
        backgroundColor: '#f4FFFF'

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
	    steps: 0.5,            
	    max: 14
          }, gridLines:{
            display:false}
        }],
        xAxes: [{
          ticks: {
	    callback: function(item, index){
	    	return index % 10== 0 ? item : null;
		},
            beginAtZero:true,
            fontSize: 11
          }, gridLines:{
            display:false}
        }]
      }
    }
  });
});
