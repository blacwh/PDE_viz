// import * as echarts from 'echarts';
d3.queue()
.defer(d3.json, 'static/data/1d_coe_e.json')
.defer(d3.json, 'static/data/1d_coe_l.json')
.await(function(err, fe, fl) {

  var chartDom = document.getElementById('coe');
  var myChart = echarts.init(chartDom);
  // var option;
  const data_e = fe;
  const data_l = fl;
  // console.log(data);
  // const DATA = data;
  const colors = ["#ff0000", "#3366ff", "#33cc33", "#9900ff", "#ff9900", "#ffff66", "#800000", "#ff66ff", "#666699", "#006600"];
  var rowData1 = [];
  var dataList1 = [];
  var rowData2 = [];
  var dataList2 = [];
  let base = ['exact', '3-order', '4-order', '5-order'];
  for (let i=1; i<11; i++) {
    rowData1.push(data_e[i]);
    rowData2.push(data_l[i]);
  };
  // console.log(rowData[0][0]);
  for (let i=0; i<rowData1.length; i++) {
    let t1 = [];
    let t2 = [];
    for (let j=0; j<base.length; j++) {
      t1.push([base[j], parseFloat(rowData1[i][j].toFixed(5))]);
      t2.push([base[j], parseFloat(rowData2[i][j].toFixed(5))])
    };
    dataList1.push(t1);
    dataList2.push(t2);
  };
  // console.log(dataList1);
  // console.log(dataList2);
  var series_e = [];
  let series_l = []
  for (let i=0; i<dataList1.length; i++) {
    var series_1 = {
        name: 'top ' + (i+1).toString(),
        type: 'line',
        smooth: false,
        symbol: 'none',
        data: dataList1[i],
        color: colors[i]
    };
    var series_2 = {
      name: 'top ' + (i+1).toString(),
      type: 'line',
      smooth: false,
      symbol: 'none',
      data: dataList2[i],
      color: colors[i]
  };
    series_e.push(series_1);
    series_l.push(series_2);
  };
  // console.log(series.length)

  option_e = {
    tooltip: {
      trigger: 'axis',
      textStyle: {fontSize: 8},
      confine: true,
      position: function (pt) {
        return [pt[0], '10%'];
      }
    },
    grid: {
      top: '10%',
      left: '10%',
      right: '10%',
      bottom: '27%'
    },
    title: {
      left: 'center',
      text: 'Candidate library',
      textStyle:{fontSize: 15},
    },
    // toolbox: {
    //   feature: {
    //   //   dataZoom: {
    //   //     yAxisIndex: 'none'
    //   //   },
    //   //   restore: {},
    //     saveAsImage: {}
    //   }
    // },
    xAxis: {
      type: 'category',
      boundaryGap: false,

    },
    yAxis: {
      type: 'value',
      boundaryGap: [0, '100%'],
      max: 1.0
    },

    dataZoom: [
      {
        type: 'slider',
        start: 0,
        end: 100,
        height: 1
      },
      {
        start: 0,
        end: 20
      }
    ],
    legend: {
        data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    },
    // legend: {
    //   bottom: 30,
    //   data: ['Beijing', 'Shanghai', 'Guangzhou'],
    //   itemGap: 20,
    //   textStyle: {
    //     color: '#fff',
    //     fontSize: 14
    //   }
    // },
    series: series_e 
  };


  option_l = {
    tooltip: {
      trigger: 'axis',
      textStyle: {fontSize: 8},
      confine: true,
      position: function (pt) {
        return [pt[0], '10%'];
      }
    },
    grid: {
      top: '10%',
      left: '10%',
      right: '10%',
      bottom: '27%'
    },
    title: {
      left: 'center',
      text: 'Candidate library',
      textStyle:{fontSize: 15},
    },
    // toolbox: {
    //   feature: {
    //   //   dataZoom: {
    //   //     yAxisIndex: 'none'
    //   //   },
    //   //   restore: {},
    //     saveAsImage: {}
    //   }
    // },
    xAxis: {
      type: 'category',
      boundaryGap: false,

    },
    yAxis: {
      type: 'value',
      boundaryGap: [0, '100%'],
      max: 0.0013
    },

    dataZoom: [
      {
        type: 'slider',
        start: 0,
        end: 100,
        height: 1
      },
      {
        start: 0,
        end: 20
      }
    ],
    legend: {
        data: ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    },
    // legend: {
    //   bottom: 30,
    //   data: ['Beijing', 'Shanghai', 'Guangzhou'],
    //   itemGap: 20,
    //   textStyle: {
    //     color: '#fff',
    //     fontSize: 14
    //   }
    // },
    series: series_l
  };

  option_e && myChart.setOption(option_e);




  $('#coe_be').on('click', function(){
    myChart.clear();
    option_e && myChart.setOption(option_e)
    $('#coe_be, #coe_bl').removeClass('selected');
    $(this).addClass('selected');
    
    // option = option_e;
    
  });


  $('#coe_bl').on('click', function(){
    myChart.clear();
    option_l && myChart.setOption(option_l)
    $('#coe_be, #coe_bl').removeClass('selected');
    $(this).addClass('selected');
    
    // option = option_e;
    
  })
});
