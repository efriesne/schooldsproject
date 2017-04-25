/////////////////////////////////////
// Some code copied from d3 project//
/////////////////////////////////////


// Chart dimensions
var margin = {top: 19.5, right: 19.5, bottom: 19.5, left: 39.5};
var width = 960 - margin.right;
var height = 500 - margin.top - margin.bottom;


// Various scales
var xScale = d3.scaleLinear().domain([-73514, -69988]).range([0, width]),
    yScale = d3.scaleLinear().domain([41244, 42871]).range([height, 0]),
    colorScale = d3.scaleOrdinal([0,1,2,3,4,5,6,7,8,9]);

// The x & y axes
var xAxis = d3.axisBottom(xScale),
    yAxis = d3.axisLeft(yScale);


// Load the data.
d3.csv("data/basic_chars_cleaned.csv", function(data) {

  data = data.filter(function(d) {
    // we're only using one year for now
    return d.year == 2013;
  })


  var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
  var dot = svg.append("g")
      .attr("class", "dots")
    .selectAll("class", "dot")
      .data(data)
    .enter()
      .append("circle")
      .attr("class", "dot")
      .call(position)
      .attr("fill", function(d) {
        return d3.schemeCategory10[colorScale(d.charter)];
      })

  var zoom = d3.zoom()
    .scaleExtent([1, 40])
    .translateExtent([[-100, -100], [width + 90, height + 100]])
    .on("zoom", zoomed);

  var view = svg.append("rect")
    .attr("class", "view")
    .attr("x", 0.5)
    .attr("y", 0.5)
    .attr("width", width - 1)
    .attr("height", height - 1)
    .attr("visibility", "hidden");

  var gX = svg.append("g")
    .attr("class", "axis axis--x")
    .call(xAxis)
    .attr("visibility", "hidden");

  var gY = svg.append("g")
    .attr("class", "axis axis--y")
    .call(yAxis)
    .attr("visibility", "hidden");

  // Add a title.


  dot.append("title")
    .text(function(d) {
      return d.name;
    })

  function zoomed() {
    svg.attr("transform", d3.event.transform);
    xAxis.scale(d3.event.transform.rescaleX(xScale));
    yAxis.scale(d3.event.transform.rescaleY(yScale));
  }

  function x(d) {
    // Return school's longitude
    return d.long*1000;
  }
  function y(d) {
      // Return school's latitude
      return d.lat*1000;
  }
  function radius(d) {
      // nothing for now
      return 5;
  }
  function color(d) {
      // Return school's charter/noncharter status
      return d.charter;
  }
  function key(d) {
      // Return school's name
      return d.name;
  }

  svg.call(zoom);


  function position(dot) {
    dot .attr("cx", function(d) {
      return xScale(x(d)); })
        .attr("cy", function(d) { return yScale(y(d)); })
        .attr("r", function(d) { return radius(d); });
}

});
