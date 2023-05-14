
let draw_line = function () {
    d3.queue()
    .defer(d3.json, 'static/data/data_true_1d.json')
    .defer(d3.json, 'static/data/data_train_1d.json')
    .await(function(err, ft, fm) {
    // console.log(ft);
    const X = ft.x;
    const U1 = ft.u;
    const U2 = fm.u;
    const xa = X.slice(0, 100);
    // console.log(X);
    var u1 = U1.slice(0, 100); // time step == 0
    var u2 = U2.slice(0, 100);
    // console.log(xa);
    // console.log(u1);
    var dataline = [];
    for (let i=0; i<100; i++) {
        var dt1 = {
            x: xa,
            y: U1.slice(i * 100, (i+1) * 100),
            type: 'scatter',
            name: 'T' + i.toString(),
            visible: false,
            color: 'blue'
        };
        var dt2 = {
            x: xa,
            y: U2.slice(i * 100, (i+1) * 100),
            type: 'scatter',
            name: 'M' + i.toString(),
            visible: false,
            color: 'green'
        };
        // dataline.push([dt1, dt2]);
        dataline.push(dt1);
        dataline.push(dt2)
    };


    var config = {
        showSendToCloud: true, 
        responsive: true,
        displayModeBar: false,
        toImageButtonOptions: {
            format: 'png',
            filename: 'isosurface',
            height: 600,
            width: 650,
        }
    };
    var steps = [];
    var a = 0;
    var b = 1;
    for (let i=0; i<dataline.length/2; i++) {
        // Plotly.addTraces('iso', data[i][0]);
        // Plotly.addTraces('iso', data[i][1]);

        var step = {
            label: i.toString(),
            method: 'update',
            args: [{
                visible: Array(dataline.length).fill(false)
            }]
        };
        step.args[0].visible[a] = true;
        step.args[0].visible[b] = true;
        a += 2;
        b += 2;
        steps.push(step);
    };

    var sliders = [{
        pad: {t: 35},
        currentvalue: {
            xanchor: 'right',
            prefix: 'time: ',
            font: {
            color: '#888',
            size: 10
            }
        },
        steps:steps
    }];
    var layout = {
        // title: 'test',
        showlegend: false,
        margin: {t:0, l:20, b:110},
        sliders: sliders
        // margin: {t:100, l:0, b:0}
    };
    // dataline[0][0].visible = true;
    // dataline[0][1].visible = true;
    dataline[2].visible = true;
    dataline[3].visible = true;
    console.log(dataline);
    console.log(steps);
    Plotly.newPlot('test', [dataline[0]], layout, config);
    for (let i=1; i<dataline.length; i++) {
        Plotly.addTraces('test', dataline[i])
    };
    
})};

draw_line();
