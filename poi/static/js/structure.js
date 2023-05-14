


const results = [{'layers': [20, 30, 40, 50, 60, 70], 'loss': 110380864.0, 'error': 0.06754666666666669, 'l1': 0.92935, 'l2': 0.9228, 'l3': 0.94521}, 
{'layers': [30, 30, 30, 30, 30, 30, 30, 30, 30], 'loss': 126167984.0, 'error': 0.06982, 'l1': 0.9317, 'l2': 0.92776, 'l3': 0.93108}, 
{'layers': [90, 90, 90, 90, 90, 90, 90, 90], 'loss': 111197616.0, 'error': 0.07371000000000001, 'l1': 0.928, 'l2': 0.92624, 'l3': 0.92463}, 
{'layers': [80, 80, 80, 80, 80, 80, 80, 80, 80], 'loss': 110356888.0, 'error': 0.07469333333333332, 'l1': 0.92612, 'l2': 0.92418, 'l3': 0.92562}, 
{'layers': [60, 50, 40, 30, 20, 10], 'loss': 134821968.0, 'error': 0.07476000000000001, 'l1': 0.94692, 'l2': 0.90565, 'l3': 0.92315}, 
{'layers': [80, 70, 60, 50, 40, 30, 20, 10], 'loss': 134848416.0, 'error': 0.0752, 'l1': 0.93089, 'l2': 0.93015, 'l3': 0.91336}, 
{'layers': [70, 70, 70, 70, 70, 70, 70, 70], 'loss': 111214136.0, 'error': 0.07565333333333335, 'l1': 0.92746, 'l2': 0.92051, 'l3': 0.92507}, 
{'layers': [50, 50, 50, 50, 50, 50, 50, 50], 'loss': 117921608.0, 'error': 0.07957000000000003, 'l1': 0.93816, 'l2': 0.8995, 'l3': 0.92363}, 
{'layers': [100, 90, 80, 70, 60, 50, 40, 30, 20, 10], 'loss': 135498416.0, 'error': 0.07982, 'l1': 0.9279, 'l2': 0.92196, 'l3': 0.91068}, 
{'layers': [40, 50, 60, 70, 80, 90, 100], 'loss': 99266856.0, 'error': 0.08083666666666667, 'l1': 0.92193, 'l2': 0.92765, 'l3': 0.90791}]


// const results = { 
//     1: [0.9969005657770025, 2.001920706147248, 1.0029586212728263],
//     2: [0.9973193419175118, 2.0014742591416397, 1.0050079553287417],
//     3: [0.9924864146763425, 1.993122079277429, 1.0009508201987023],
//     4: [1.0053876601594742, 2.0066174707652586, 0.9958248374796341],
//     5: [0.9967852978933144, 1.996506660679261, 0.9930076464598978, 0.9966211422963457, 0.994881918855133, 1.0059276661839518],
//     6: [0.9997131666790389, 2.0020839246882645, 0.990953490558544, 0.994120184467762, 1.0087179501041532, 1.0028074669129272],
//     7: [0.9973917076920785, 1.9916750103321148, 1.001737021048339, 0.9955093081693045, 1.0045619370931076, 1.0072970680520512],
//     8: [0.9952576234986882, 2.0066046851817068, 1.003508651939641, 0.992320902860208, 0.9969447762292662, 0.9922475345331851],
//     9: [0.9963477444000894, 2.008083096134174, 1.006169724318491, 1.0077238420455525, 1.0006442311173531, 1.0073493507845188],
//     0: [1.006470481379117, 2.0100064449186164, 1.0044481449164213, 1.0063343210247153, 1.0022992248647045, 1.0047363828964255]
//     }



    let draw_s = function(b_id) {
        var width = 1310,
                height = 300,
                nodeSize = 10;
    
        let draw_ss = function(data_s) {
            d3.select("#str").select("svg").remove();
            var svg = d3.select("#str").append("svg")
                        .attr("width", width)
                        .attr("height", height);
        d3.json(data_s, function(data_sj){
            var nodes = data_sj.nodes;
    
            // get network size
            var netsize = {};
            nodes.forEach(function (d) {
                if(d.layer in netsize) {
                    netsize[d.layer] += 1;
                } else {
                    netsize[d.layer] = 1;
                }
                d["lidx"] = netsize[d.layer];
            });
    
            // calc distances between nodes
            var largestLayerSize = Math.max.apply(
                null, Object.keys(netsize).map(function (i) { return netsize[i]; }));
    
            var xdist = width / Object.keys(netsize).length,
                ydist = height / largestLayerSize;
    
            // create node locations
            nodes.map(function(d) {
                d["x"] = (d.layer - 0.5) * xdist;
                d["y"] = (d.lidx - 0.5) * ydist;
            });
    
            // autogenerate links
            var links = [];
            nodes.map(function(d, i) {
                for (var n in nodes) {
                if (d.layer + 1 == nodes[n].layer) {
                    links.push({"source": parseInt(i), "target": parseInt(n), "value": 1}) }
                }
            }).filter(function(d) { return typeof d !== "undefined"; });
    
            // draw links
            var link = svg.selectAll(".link")
                .data(links)
                .enter().append("line")
                .attr("class", "link")
                .attr("x1", function(d) { return nodes[d.source].x; })
                .attr("y1", function(d) { return nodes[d.source].y; })
                .attr("x2", function(d) { return nodes[d.target].x; })
                .attr("y2", function(d) { return nodes[d.target].y; })
                .style("stroke-width", function(d) { return Math.sqrt(d.value); });
    
            // draw nodes
            var node = svg.selectAll(".node")
                .data(nodes)
                .enter().append("g")
                .attr("transform", function(d) {
                    return "translate(" + d.x + "," + d.y + ")"; }
                );
    
            var circle = node.append("circle")
                .attr("class", "node")
                .attr("r", nodeSize)
                .style("fill", '#323392')
                // function(d) { return color(d.layer); });
                });
    
        }
    
        // let color = d3.scaleOrdinal(d3.schemeCategory10);
        const head = "static/data/"
        // let nn = document.getElementById('nn').innerHTML.slice(-1);
        
        let nn = b_id.slice(-1);
        
        let data_s = head + "data" + nn + ".json";
        // console.log(data_s);
        draw_ss(data_s);
    };
    
    // let draw_l = function(b_id) {
    //     d3.queue()
    //     .defer(d3.json, 'static/data/1d_dz_e.json')
    //     .defer(d3.json, 'static/data/1d_dz_l.json')
    //     .await(function(err, fe, fl) {
    //         if (err) {
    //             console.error('failed:' + err);
    //         }
    //         else {
    //             let rank = parseInt(b_id.slice(-1)) - 1;
    //             rank =  rank === -1 ? 9 : rank;
    //             // console.log(rank);
    //             let myChart_l = echarts.init(document.getElementById("line"));
    //             let option;
            
    //             option = {
    //                 xAxis: {
    //                     type: "log",
            
    //                 },
    //                 yAxis: {
    //                     type: "log"
    //                 },
    //                 toolbox: {
    //                     feature: {
    //                         saveAsImage: {}
    //                     }
    //                 },
    //                 tooltip: {
    //                     trigger: 'axis',
    //                     axisPointer: {
    //                         label: {
    //                             fontStyle: 'italic',
    //                             precision: 0
    //                         }
    //                 }
    //                 },
    //                 legend: {
    //                     data: ['Derivation error', 'NN loss']
    //                 },
    //                 toolbox: {
    //                     feature: {
    //                         saveAsImage: {}
    //                     }
    //                 },
    //                 series: [
    //                 {   
    //                     name: 'NN loss',
    //                     data: fl[rank],
    //                     type: 'line'
    //                 },
    //                 {
    //                     name: 'Derivation error',
    //                     data: fe[rank],
    //                     type: 'line'
    //                 }
    //                 ]
    //             };
            
    //             myChart_l.setOption(option);
    //         }
    //     })
        
    // }
            
    
    let write_r = function(b_id) {
        var coe = {};
        for (let i=0; i<results.length; i++) {
            var ct = [];
            ct.push(results[i].l1);
            ct.push(results[i].l2);
            ct.push(results[i].l3);
            if (!((i+1)===10)) {
                coe[i+1] = ct;
            }
            else {
                coe[0] = ct;
            }  
        };

        // console.log(coe);
        let rank = parseInt(b_id.slice(-1));
        // let result = "$f=u_t+%.5fu_x+%.5fu_y+%.5fu_z-%.5fu_{xx}-%.5fu_{yy}-%.5fu_{zz}$" % tuple(results[rank + 1])
        let lam = [];
        // console.log(coe);
        // console.log(coe[rank][0].toFixed(4));
        // lam.push(coe[rank][0].toFixed(4));
        for(let i=0; i<=3; i++){
            lam.push(coe[rank][i]);
        }
        let template = "R: " + `f = ${lam[0]}u_xx - ${lam[1]}u_yy + ${lam[2]}u_zz`;
        // let template = Std：$f=u_t+u_x+2u_y+u_z-u_{xx}-u_{yy}-u_{zz}$;
        // var math = '\\frac{1}{\\sqrt{x^2 + 1}}';
        var el = document.getElementById("exp");
        el.textContent = template;
        // MathJax.Hub.Queue(["Typeset", MathJax.Hub, el]);
        // $("#exp").latex();
        
    }
    
    
    
    let rb1 = $("#s1"), rb2 = $("#s2"), rb3 = $("#s3"), rb4 = $("#s4"), rb5 = $("#s5"), rb6 = $("#s6"), rb7 = $("#s7"), rb8 = $("#s8"), rb9 = $("#s9"), rb10 = $("#s10");
    
    $("#s1, #s2, #s3, #s4, #s5, #s6, #s7, #s8, #s9, #s10").click(function(){
        console.log('clicked', this.id);
        $("#s1, #s2, #s3, #s4, #s5, #s6, #s7, #s8, #s9, #s10").removeClass('active');
        $(this).addClass('active');
        
        draw_s(this.id);
        // draw_l(this.id);
        write_r(this.id);
    });