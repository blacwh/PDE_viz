    
d3.json('static/data/data_true_1d.json', function(err, data) {
    const X = data.x;
    const U = data.u;
    // console.log(X);
    var u1 = U.slice(0, 100); // time step == 0
    var d1 = [];
    for(let i=0; i<10; i++) {
        d1.push(u1.slice(i*10, (i+1)*10));
        // var temp = [];
        // for(let j=0; j<10; j++) {
        //     temp.push(u1[i*10 + j]);
        // }
    }
    console.log(d1)
    var c_data = [ {
        z: 
        d1,
        // [
        //     [0.22,0.24,0.35,0.44,0.31],
        //     [0.19,0.21,0.34,0.45,0.32]
            // [1,2,3,4,5,6,7,8,9,10],
            // [2,3,4,5,6,7,8,9,10,11],
            // [1,2,2,3,5,6,7,8,9,20],
            // [1,4,3,4,5,6,7,8,9,20],
            // [5,2,3,4,5,6,4,8,9,10],
            // [1,2,3,4,5,6,3,8,9,10],
            // [1,2,3,4,5,2,7,8,9,20],
            // [1,2,3,1,1,6,7,8,9,20],
            // [3,4,5,6,7]
            // [10, 10.625, 12.5, 15.625, 20],
            //  [5.625, 6.25, 8.125, 11.25, 15.625],
            //  [2.5, 3.125, 5., 8.125, 12.5],
            //  [0.625, 1.25, 3.125, 6.25, 10.625],
            //  [0, 0.625, 2.5, 5.625, 10]
            // ],
        type: 'contour',
        colorscale: 'RdBu',
        contours:{
        coloring: 'lines'
        }
    }];
    
    var layout = {
        title: 'Contour Lines'
    };
    
    Plotly.newPlot('test', c_data, layout);
})    
