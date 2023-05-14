// let data = [[ 11.392735, 12.677128, "#ff0000" ],
// [-15.291774,  -43.817154, "#3366ff" ],
// [ 23.509134,   42.682472, "#33cc33" ],
// [ -5.8055058, -13.491217, "#9900ff" ],
// [ 42.702374,    4.499076, "#ff9900" ],
// [-42.120872,  -14.238836, "#ffff66" ],
// [-19.870193,   14.45868, "#800000"  ],
// [-49.864685,   24.943441, "#ff66ff" ],
// [-13.5905075,  47.130478, "#666699" ],
// [ 24.159649,  -27.938028, "#006600" ]];

let data = [[ 12.118236,   -0.8968876, "#ff0000"],
[-35.42707,  11.139284, "#3366ff" ],
[-35.462765,  -18.857016, "#33cc33" ],
[ -6.859614,  -37.787167, "#9900ff" ],
[-10.401239,  -12.056181, "#ff9900" ],
[ 16.201273,   27.989113, "#ffff66" ],
[ -8.785016,   13.025376, "#800000" ],
[ 20.770372,  -26.146297, "#ff66ff" ],
[ 37.18753,    3.787139, "#666699" ],
[-14.289074,   37.923836, "#006600" ]];

let dict = {};
let selected = new Set();
for(let i = 0; i < data.length; i++) {
    dict[data[i][0]] = i + 1;
    selected.add(i+1);
}

// let colormap = require("colormap");

// let colors = colormap({
//     colormap: "rdbu",
//     nashades: 10,
//     format: "hex",
//     alpha: 1
// });
// let colors = ["#ff00ff", "#99ffcc", "#0066ff", "#66ff33", "#ff9900", "#ff0000", "#663300", "#669999", "#ffff66", "#9900cc"]
let colors = ["#ff0000", "#3366ff", "#33cc33", "#9900ff", "#ff9900", "#ffff66", "#800000", "#ff66ff", "#666699", "#006600"]

var new_data = [[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null]];
// new Array(10).fill( new Array(11).fill(null));

let draw_np = function(s) {
    // console.log(s.has(1));
    new_data = [[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null],
[null,null,null,null,null,null,null,null,null,null,null]];
    // console.log(new_data[0]);
    for (let i=1; i <= 10; i++) {
        if (s.has(i)) {
            // console.log(new_data[0]);
            for (let j=1; j <= 10; j++) {
                // console.log(i,j)
                // console.log(new_data[0])
                // console.log(new_data[1])
                new_data[i-1][j-1] = g1_data[i-1][0][j-1];
            }
            new_data[i-1][10] = g1_data[i-1][1][19];
            new_data[i-1][11] = g1_data[i-1][2];
        }
    }
    
    
    draw_p(new_data);
}



let draw = () => {

    const svg = d3.select("#atr")
                .call(d3.zoom().on("zoom", function() {
                    svg.attr("transform", d3.event.transform)
                }))
                .append("g")

                svg.selectAll('.circle')
                .data(data)
                .enter().append('circle')
                .on('click', function(d){
                    if (selected.has(dict[d[0]])) {
                        selected.delete(dict[d[0]]);
                        d3.select(this).style("fill", "white");
                        draw_np(selected);
                    }
                    else {
                        selected.add(dict[d[0]]);
                        d3.select(this).style("fill", d[2]);
                        draw_np(selected);
                    }
                    // console.log(new_data[0])
                    // console.log(selected);
                })



                .style("stroke", (d, i) => {
                    return colors[i]
                })
                .style("stroke-width", 2)
                .attr('cx', (d) => {
                    return d[0] * 6;
                })
                .attr('cy', (d) => {
                    return d[1] * 6;
                })
                .attr('r', 20)
                .attr('fill', (d, i) => {
                    return colors[i]
                })
            }

let b = document.getElementById("atrplot_b");
b.addEventListener("click", () => {
    draw()
});
