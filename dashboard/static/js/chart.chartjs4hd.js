$(function(){
    'use strict';
  
    var ctx1 = document.getElementById('chartst24H').getContext('2d');
    var myChart1 = new Chart(ctx1, {
      type: 'line',
      data: {
        labels: time,
        datasets: [{
          data: hd,
          borderColor:'#ADD8E6',
          label: '# Votes ',
          backgroundColor: '#ADDDD6'
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
              //beginAtZero:true,
              fontSize: 10,
	      stepValue:0.5,
              //max: 80
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
  