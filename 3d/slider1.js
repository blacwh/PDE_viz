
let iso_draw = function()     
{
    d3.queue()
    .defer(d3.json, 'static/data/true.json')
    .defer(d3.json, 'static/data/train.json')
    .await(function(error, f1, f2){
        if (error) {
            console.error('failed:' + error);
        }
        else {
            const X = f1.x;
            const Y = f1.y;
            const Z = f1.z;

            const u1 = f1.u;
            const u2 = f2.u;

            // construct data
            var data = [];
            for (let i=0; i<30; i++) {
                var u1_temp = u1.slice(i*1000, (i+1)*1000);
                var u2_temp = u2.slice(i*1000, (i+1)*1000);
                var d1 = [{
                    type: "isosurface",
                    name: 'T: ' + i.toString(),
                    x: X,
                    y: Y,
                    z: Z,
                    value: u1_temp,
                    visible: false,
                    isomin: 0.0,
                    isomax: 1.0,
                    surface: {show: true, count: 5},
                    colorscale: "Blues",
                    caps: {
                        x:{
                            show: false
                        },
                        y:{
                            show: false
                        },
                        z:{
                            show: false
                        }
                    },

                    colorbar: {
                        title: {text: 'T', side: 'bottom'},
                        thickness: 10,
                        tickfont: {size: 10},
                        nticks: 4,
                        orientation: 'h',
                        len: 1,
                        y: 0.9,
                        x: 0.5,
                        // y: 0
                        ypad: 0
                    },
                }];
                var d2 = [{
                    type: "isosurface",
                    name: 'M: ' + i.toString(),
                    x: X,
                    y: Y,
                    z: Z,
                    value: u2_temp,
                    visible: false,
                    isomin: 0.0,
                    isomax: 1.0,
                    surface: {show: true, count: 5},
                    colorscale: "Greens",
                    caps: {
                        x:{
                            show: false
                        },
                        y:{
                            show: false
                        },
                        z:{
                            show: false
                        }
                    },

                    colorbar: {
                        title: {text: 'M', side: 'top'},
                        thickness: 10,
                        tickfont: {size: 10},
                        nticks: 4,
                        ticklabelposition: 'outside right',
                        xpad: 0,
                        len: 0.8
                    },
                }];
                // data.push([d1, d2])
                data.push(d1);
                data.push(d2)
            };
            console.log('data: ', data);
            var config = {
                showSendToCloud: true, 
                responsive: true,
                displayModeBar: false
            };
            // var layout = {

            //     showlegend: true,
            //     margin: {t:0, l:20, b:0},

            // };
            console.log(data[0][0]);
            data[0].visible = true;
            data[1].visible = true;
            // newplot requires array
            // Plotly.newPlot('iso', data[1], layout, config);
            // addTraces requires no array
            // Plotly.addTraces('iso', data[0]);
            // Plotly.addTraces('iso', data[2]);
            // Plotly.addTraces('iso', data[3]);
            // var steps = [null, null];
            // steps[0] = {
            //     // label: 'd3',
            //     method: 'update',
            //     args: [{
            //         visible: [true, true, false, false]
            //     }]
            // };
            // steps[1] = {
            //     // label: 'd3',
            //     method: 'update',
            //     args: [{
            //         visible: [false, false, true, true]
            //     }]
            // };


            var steps = [];
            var a = 0;
            var b = 1;
            for (let i=0; i<data.length/2; i++) {
                var step = {
                    // labels: 't: ' + i.toString(),
                    method: 'update',
                    args: [{
                        visible: Array(data.length).fill(false)
                    }]
                };
                // let j = i;
                step.args[0].visible[a] = true;
                step.args[0].visible[b] = true;
                a += 2;
                b += 2;
                
                steps.push(step);
            };
            console.log(steps);
            var sliders = [{
                pad: {t: 30},
                currentvalue: {
                    xanchor: 'right',
                    prefix: 'time: ',
                    font: {
                    color: '#888',
                    size: 10
                    }
                },
                // active: 1,
                steps:steps
            }]
            // Plotly.newPlot('iso', data[0][0], layout, config);
            // Plotly.addTraces('iso', data[0][1]);
            // Plotly.newPlot('iso', data[0], layout, config);
            // for (let i=1; i<data.length; i++) {
            //     // Plotly.addTraces('iso', data[i][0]);
            //     // Plotly.addTraces('iso', data[i][1]);
            //     Plotly.addTraces('iso', data[i]);
            // }
            var layout = {
                // title: 'test',
                showlegend: true,
                margin: {t:0, l:20, b:0},
                sliders: sliders
                // margin: {t:100, l:0, b:0}
            };

            Plotly.newPlot('iso', data[0], layout, config);
            // Plotly.relayout('iso', layout);
            for (let i=1; i<data.length; i++) {
                Plotly.addTraces('iso', data[i])
            };
            // Plotly.addTraces('iso', data[1]);
            // Plotly.addTraces('iso', data[2]);
            // Plotly.addTraces('iso', data[3]);
            // Plotly.addTraces('iso', data2);
            console.log('end');
        }
    });
};

iso_draw();

            // Plotly.newPlot('iso', data[0][0], layout, config);
            // Plotly.addTraces('iso', data[0][1]);

            
            

            // var v1 = u1.slice(0, 1000);
            // var v2 = u2.slice(0, 1000);
            // console.log(X.length, Y.length, Z.length);
            // console.log(v1.length);
        