// import * as echarts from 'echarts';

var chartDom = document.getElementById('tt');
var myChart = echarts.init(chartDom);
var option;

// let base = +new Date(1988, 9, 3);
// let oneDay = 24 * 3600 * 1000;
// let data = [[base, Math.random() * 300]];
// for (let i = 1; i < 20000; i++) {
//   let now = new Date((base += oneDay));
//   data.push([+now, Math.round((Math.random() - 0.5) * 20 + data[i - 1][1])]);
// }
let base = [0,1,2,3,4,5,6,7,8,9,10];
let data = [];
for (let i=0;i<base.length;i++) {
    let a = base[i];
    let b = base[i] * 2;
    data.push([a, b]);
}
option = {
  tooltip: {
    trigger: 'axis',
    position: function (pt) {
      return [pt[0], '10%'];
    }
  },
  title: {
    left: 'center',
    text: 'Large Ara Chart'
  },
//   toolbox: {
//     feature: {
    //   dataZoom: {
    //     yAxisIndex: 'none'
    //   },
    //   restore: {},
    //   saveAsImage: {}
    // }
//   },
  xAxis: {
    type: 'value',
    boundaryGap: false
  },
  yAxis: {
    type: 'value',
    boundaryGap: [0, '100%']
  },
  height:200,
  dataZoom: [
    // {
    //     moveHandleStyle: {
    //     color: 'rgb(255,255,255)',

    // }},
    {
      type: 'slider',
      start: 0,
      end: 10,
      height: 10,
    //   bottom: 20
    //   handleSize: '100%'
    //   moveHandleSize: 0,
    //   backgroundColor: 'rgb(255, 0, 0)'
    },
    {
      start: 0,
      end: 100
    }
  ],
  series: [
    {
      name: 'Fake Data',
      type: 'line',
      smooth: true,
      symbol: 'none',
    //   areaStyle: {},
      data: data
    }
  ]
};

option && myChart.setOption(option);
