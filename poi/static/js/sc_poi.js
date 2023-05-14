d3.queue()
    .defer(d3.json, 'static/data/poi.json')
    .defer(d3.json, 'static/data/poi_m.json')
    .await(function(error, f1, f2){
        if (error) {
            console.log('error: ', error)
        }
        else {
            const dt = f1;
            const dm = f2;
            
            const x1 = dt.x;
            const y1 = dt.y;
            const z1 = dt.z;
            const p1 = dt.p;

            const x2 = dm.x;
            const y2 = dm.y;
            const z2 = dm.z;
            const p2 = dm.p;
            var data1 = {
                x: x1,
                y: y1,
                z: z1,
                mode: 'markers',
                marker: {
                    size: 1,
                    color: p1,
                    colorscale: 'RdBu',
                    colorbar: {
                        thickness: 10
                    },
                    // reversescale: true
                },
                type: 'scatter3d'
            };

            var data2 = {
                x: x2,
                y: y2,
                z: z2,
                mode: 'markers',
                marker: {
                    size: 1,
                    color: p2,
                    colorscale: 'RdBu',
                    colorbar: {
                        thickness: 10
                    },
                    // reversescale: true
                },
                type: 'scatter3d'
            };

            var layout1 = {
                l: 0,
                r: 0,
                b: 0,
                t: 0,
                title: 'Ground truth',
                // showlegend: false
            };
            var layout2 = {
                l: 0,
                r: 0,
                b: 0,
                t: 0,
                title: 'Model data'
            };
            Plotly.newPlot('sc1', [data1], layout1, {displayModeBar: false});
            Plotly.newPlot('sc2', [data2], layout2, {displayModeBar: false});
        }
    })