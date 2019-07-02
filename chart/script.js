const json = '../get_data.json';

document.addEventListener('DOMContentLoaded', function () {
    fetch(json)
        .then(function (response) {
            return response.json();
        })
        .then(function (data) {
            let parsedData = parseData(data);
            drawChart(parsedData);
        })
        .catch(function (err) {
            console.log(err);
        })
});

function parseData(data) {
    let arr = [];

    for (let i=0; i < data.length; i++) {
        arr.push({
            date: data[i].time.time,
            value: data[i].value.value
        });
    }
    console.log(arr);
    return arr;
}

function drawChart(data) {
    const svgWidth = 1600, svgHeight = 400;
    const margin = {top: 20, right: 20, bottom: 30, left: 50};
    const width = svgWidth - margin.left - margin.right;
    const height = svgHeight - margin.top - margin.bottom;

    let svg = d3.select('svg').attr("width", svgWidth).attr("height", svgHeight);
    let g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
    let x = d3.scaleTime().rangeRound([0, width]);
    let y = d3.scaleLinear().rangeRound([height, 0]);
    let line = d3.line().x(function (d) {return x(d.date)}).y(function (d) {return y(d.value)});

    x.domain(d3.extent(data, function (d) {return d.date}));
    y.domain(d3.extent(data, function (d) {return d.value}));

    g.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x))
        .select(".domain");

    g.append("g")
        .call(d3.axisLeft(y))
        .append("text")
        .attr("fill", "#000")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", "0.71em")
        .attr("text-anchor", "end")

    g.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("stroke-width", 1.5)
        .attr("d", line);
}

