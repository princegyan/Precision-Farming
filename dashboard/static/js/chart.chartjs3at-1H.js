$(function(){
  'use strict';

  var ctx1 = document.getElementById('chartat1H').getContext('2d');
  var myChart1 = new Chart(ctx1, {
    type: 'line',
    data: {
      labels: time,
      datasets: [{
        data: a_temp,
        borderColor: 'red',
        label: 'Temperature',
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
            
            fontSize: 10,
	    steps: 0.5,
	    stepValue: 0.1,
           
            //beginAtZero: true,
            fontSize: 10,
	    steps: 0.5,
	   // stepValue: 0.5,
            //max: 40
          }, gridLines:{
            display:false}
        }],
        xAxes: [{
          ticks: {

	    callback: function(item, index){
	    	return index % 10 == 0 ? item : null;
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
