// import * as echarts from 'echarts';
d3.json('static/data/top10_coe.json', function(data) {
  var chartDom = document.getElementById('coe');
  var myChart = echarts.init(chartDom);
  var option;


  // console.log(data);
  // const DATA = data;
  const colors = ["#ff0000", "#3366ff", "#33cc33", "#9900ff", "#ff9900", "#ffff66", "#800000", "#ff66ff", "#666699", "#006600"];
  var rowData = []
  var dataList = []
  let base = ['exact', '2-order', '3-order'];
  for (let i=1; i<11; i++) {
    rowData.push(data[i]);
  };
  // console.log(rowData[0][0]);
  for (let i=0; i<rowData.length; i++) {
    let t = [];
    for (let j=0; j<base.length; j++) {
      t.push([base[j], parseFloat(rowData[i][j].toFixed(5))])
    };
    dataList.push(t)
  };
  console.log(dataList);
  var series = [];
  for (let i=0; i<dataList.length; i++) {
    var series_1 = {
        name: 'top ' + (i+1).toString(),
        type: 'line',
        smooth: false,
        symbol: 'none',
        data: dataList[i],
        color: colors[i]
    };
    series.push(series_1)
  };
  console.log(series.length)
  // var dataList = []
  // for (let i=0; i<base.length; i++) {
  //   dataList.push([base[i], rowData])
  // }

  // let base = +new Date(1988, 9, 3);
  // let oneDay = 24 * 3600 * 1000;
  // let data = [[base, Math.random() * 300]];
  // for (let i = 1; i < 20000; i++) {
  //   let now = new Date((base += oneDay));
  //   data.push([+now, Math.round((Math.random() - 0.5) * 20 + data[i - 1][1])]);
  // }
  // let base = [0,1,2,3,4,5,6,7,8,9,10];
  // // let data = [];
  // let data1 = [];
  // for (let i=0;i<base.length;i++) {
  //     let a = base[i];
  //     let b = base[i] * 2;
  //     // data.push([a, b]);
  //     data1.push([a, a*1.5])
  // };
  // console.log(data1);
  option = {
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
        start: 1,
        end: 20,
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
    series: series 
    // [
    //   {
    //     name: '1',
    //     type: 'line',
    //     smooth: true,
    //     symbol: 'none',
    //   //   areaStyle: {},
    //     // data: data
    //   },
    //   {
    //       name: '2',
    //       type: 'line',
    //       smooth: true,
    //       symbol: 'none',
    //       data: data1
    //   }
    // ]
  };

  option && myChart.setOption(option);

});
