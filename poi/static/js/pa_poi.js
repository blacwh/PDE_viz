    
const draw_p = function() {
    d3.json('static/data/padata.json', function(err, data) {
        if (err) {
            console.log('error: ', err)
        };
    var chartDom = document.getElementById('paint_id');
    var myChart = echarts.init(chartDom);
    var option;
    var dims = [];
    const colors = ["#ff0000", "#3366ff", "#33cc33", "#9900ff", "#ff9900", "#ffff66", "#800000", "#ff66ff", "#666699", "#006600"];
    for (let i=0; i<10; i++) {
        var dim = {
            dim: i,
            name: 'layer',
            max: 100,
            min: 0,
            scale: false,
            nameLocation: 'center',  
            nameGap: 15,
            nameRotate: 0, 
            nameTextStyle: {
                fontSize: '15px',
                fontWeight: 'bolder'
            }
        };
        dims.push(dim)
    };
    // var cat = ['dense', 'increment', 'decrement'];

    dims.push({
        dim: dims.length,
        name: 'Loss',
        type: 'log',
        min: 0.98,
        max: 1.40000000,
        scale: false,
        nameLocation: 'center',
        nameGap: 15,
        nameRotate: 0, 
        nameTextStyle: {
            fontSize: '15px',
            fontWeight: 'bolder'
        }
    });
    dims.push({
        dim: dims.length,
        name: 'Error',
        type: 'log',
        min: 0.06,
        max: 0.085,
        scale: false,
        nameLocation: 'center',
        nameGap: 15,
        nameRotate: 0, 
        nameTextStyle: {
            fontSize: '15px',
            fontWeight: 'bolder'
        }
    });
    console.log(dims);
    var series = [];
    // console.log(data[1].slice(0, -2))
    for (let i=1; i<11; i++) {
        var s = {
            type: 'parallel',
            coordinateSystem: "parallel",
            lineStyle: {
                show: true,
                width: 5.2 - 0.2 * i,
                opacity: 1,
                curveness: 0,
                type: "solid",
                color: colors[i-1]
            },
            name: data[i][12],
            data: [data[i].slice(0, -1)],
            smooth: false
        };
        series.push(s)
    };
    console.log(series);
    option = {
    parallelAxis: dims,
    //   [
    //     { dim: 0, name: 'Price' },
    //     { dim: 1, name: 'Net Weight' },
    //     { dim: 2, name: 'Amount' },
    //     {
    //       dim: 3,
    //       name: 'Score',
    //       type: 'category',
    //       data: ['Excellent', 'Good', 'OK', 'Bad']
    //     }
    //   ],
    // toolbox: {feature: {
    //     saveAsImage: {}
    // }},
    parallel: {
        "left": "5%",
        "right": "13%",
        "bottom": "10%",
        "top": "20%"
        },
    tooltip: {
        show: true,
        trigger: 'item',
        triggerOn: 'mousemove|click',
        backgroundColor: '#9966ff',
        padding: 10,
        borderColor: '#cccccc',
        borderWidth: 1,
        textStyle: {
            color: "#fff"
        }
    },
    series: series
    };

    option && myChart.setOption(option);
})};

const btn_p = document.getElementById("display");
// btn_p.addEventListener("click", draw_p(new_data2));

// btn_p.addEventListener("click", new_data2 => {
//     draw_p(new_data2)
// });

btn_p.addEventListener('click', function() {
    draw_p(), false;
})
