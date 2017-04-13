/////////////////////////////////////
// Step 1: Write accessor functions //
//////////////////////////////////////



// Chart dimensions
var margin = {top: 19.5, right: 19.5, bottom: 19.5, left: 39.5};
var width = 960 - margin.right;
var height = 500 - margin.top - margin.bottom;


// Various scales

var xScale = d3.scaleLinear().domain([-73514, -69988]).range([0, width]),
    yScale = d3.scaleLinear().domain([41244, 42871]).range([height, 0]),
    colorScale = d3.scaleOrdinal([0,1]);

// The x & y axes
var xAxis = d3.axisBottom(xScale),
    yAxis = d3.axisLeft(yScale);

// Create the SVG container and set the origi

//////////////////////////////
// Step 2: Add x and y axes //
//////////////////////////////
  // svg.append("g")
  //   .attr("class", "axis line")
  //   .call(yAxis)
  //   .append("g")
  //   .attr("class", "axis line")
  //   .attr("transform", "translate(0, " + height + ")")
  //   .call(xAxis);

//////////////////////////////////////
// Step 3: Add axis and year labels //
//////////////////////////////////////

// var x = svg.append("text")
//     .text("x-axis")
//     .attr("class", "label")
//     .attr("transform", "translate(" + height + "," + (height + 15) + ")");

// var y = svg.append("text")
//     .text("y-axis")
//     .attr("class", "label")
//     .attr("transform", "translate(" + -1*margin.left + "," + height/2 + ")")

///////////////////////////
// Step 4: Load the data //
///////////////////////////

// Load the data.
d3.json("../data/basic_chars_cleaned.json", function(data) {

  data = data.filter(function(d) {
    return d.year == 2013;
  })

  console.log(d3.schemeCategory10[colorScale(data[0].charter)])

  /////////////////////////////////////////
  // Functions provided for your utility //
  /////////////////////////////////////////

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

  ///////////////////////////////////
  // Step 5: Add fluff and overlay //
  ///////////////////////////////////

  // Add a title.


  dot.append("title")
    .text(function(d) {
      return d.name;
    })


  function x(d) {
    // Return nation's income
    return d.long*1000;
  }
  function y(d) {
      // Return nation's lifeExpectancy
      return d.lat*1000;
  }
  function radius(d) {
      // Return nation's population
      return 5;
  }
  function color(d) {
      // Return nation's region
      return d.charter;
  }
  function key(d) {
      // Return nation's name
      return d.name;
  }

  function position(dot) {
    dot .attr("cx", function(d) {
      return xScale(x(d)); })
        .attr("cy", function(d) { return yScale(y(d)); })
        .attr("r", function(d) { return radius(d); });
}

});
