// Plotly.newPlot('myDiv');
var data1 = {
    x: [1, 2, 3, 5], 
    y: [2, 1, 3, 8],
    mode: 'markers',
    type: 'scatter',
    // visible: true
}
;
var data2 = {
    x: [2, 3, 4, 5],
    y: [16, 5, 11, 9],
    mode: 'markers',
    type: 'scatter',
    // visible: true
  };

var data3 = {
    x: [1, 2, 3, 4],
    y: [10, 15, 13, 17],
    mode: 'markers',
    type: 'scatter',
    // visible: true
    };

var data4 = {
    x: [2, 3, 5, 3],
    y: [11, 16, 14, 12],
    mode: 'markers',
    type: 'scatter',
    // visible: true
    };
var data = [data1, data2, data3, data4];

Plotly.newPlot('myDiv', [data1, data2]);

var steps = [null, null, null, null];
steps[0] = {
    label: 'd1',
    method: 'update',
    args: [{
        visible: [false, false, false, false]
    }]
};
steps[1] = {
    label: 'd2',
    method: 'update',
    args: [{
        visible: [false, true, false, true]
    }]
};
steps[2] = {
    label: 'd3',
    method: 'update',
    args: [{
        visible: [true, true, true, true]
    }]
};
steps[3] = {
    label: 'd3',
    method: 'update',
    args: [{
        visible: [true, false, true, true]
    }]
};

var layout = {
    sliders: [{
      pad: {t: 30},
      currentvalue: {
        xanchor: 'right',
        prefix: 'data: ',
        font: {
          color: '#888',
          size: 20
        },

      },
    //   active: 1,
    //   bgcolor: '#ff0000',
      steps: steps
    //   [{
    //     label: 'd1',
    //     method: 'update',
    //     args: [{
    //         'visible': [true, false, false]
    //     }]
    //   }, {
    //     label: 'd2',
    //     method: 'update',
    //     args: [{
    //         'visible': [false, true, false]
    //     }]
    //   }, 
    //   {
    //     label: 'd3',
    //     method: 'update',
    //     args: [{
    //         'visible': [false, false, true]
    //     }]
    //   }]
    }]
  };

// Plotly.update('myDiv', data, layout);
Plotly.addTraces('myDiv', [data3, data4]);
// Plotly.addTraces('myDiv', data2);
// Plotly.addTraces('myDiv', data3);
// Plotly.addTraces('myDiv', data4);

Plotly.relayout('myDiv', layout);


