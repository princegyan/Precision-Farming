function tripSpeedsLineGraph() {
    var gpsData = @Html.Raw(Json.Serialize(Model.gpsData));

    chartData = []
    var reqData = $.map(gpsData, function (value, index) {
         chartData.push([new Date(value.timestamp), value.sp]);
    });

    var chart = Highcharts.chart('tripSpeedsLineChart', {
        chart: {
            type: 'spline',
            zoomType: 'x',
            panning: true,
            panKey: 'shift'
        },
        title: {
            text: "Speed during trip"
        },
        subtitle: {
            text: 'Click and drag to zoom in. Hold down shift key to pan.'
        },
        xAxis: {
            type: 'datetime',
            dateTimeLabelFormats: {
                day: '%b %H:%M:%S'
            },
            title: {
                text: 'Time of day'
            }
        },
        yAxis: {
            title: {
                text: 'Speed'
            },
            min: 0
        },
        tooltip: {
            crosshairs: [true],
            formatter: function () {
                return "Datetime: " + moment.utc(moment.unix(this.x/1000)).format("DD/MM-YYYY HH:mm:ss") + "<br> Speed: " + this.y;
            }
        },
        series: [{
            name: 'Speed Data',
            data: chartData
        }]
    });
}