/////////////////////////////////////
// Step 1: Write accessor functions //
//////////////////////////////////////

// Accessor functions for the four dimensions of our data
// For each of these, assume that d looks like the following:
// {"name": string, "income": number, "lifeExpectancy": number,
//  "population": number, "region": string}


//////////////
// Provided //
//////////////

// Chart dimensions
var margin = {top: 19.5, right: 19.5, bottom: 19.5, left: 39.5};
var width = 960 - margin.right;
var height = 500 - margin.top - margin.bottom;


// Various scales

var xScale = d3.scaleLog().domain([-735143, -699886]).range([0, width]),
    yScale = d3.scaleLinear().domain([412447, 428719]).range([height, 0]),
    radiusScale = d3.scaleSqrt().domain([0, 5e8]).range([0, 40]),
    colorScale = d3.scaleOrdinal([0, 1, 2, 3, 4, 5, 6]);

// The x & y axes
var xAxis = d3.axisBottom(xScale),
    yAxis = d3.axisLeft(yScale);

// Create the SVG container and set the origin
var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

//////////////////////////////
// Step 2: Add x and y axes //
//////////////////////////////
  svg.append("g")
    .attr("class", "axis line")
    .call(yAxis)
    .append("g")
    .attr("class", "axis line")
    .attr("transform", "translate(0, " + height + ")")
    .call(xAxis);

//////////////////////////////////////
// Step 3: Add axis and year labels //
//////////////////////////////////////

var x = svg.append("text")
    .text("x-axis")
    .attr("class", "label")
    .attr("transform", "translate(" + height + "," + (height + 15) + ")");

var y = svg.append("text")
    .text("y-axis")
    .attr("class", "label")
    .attr("transform", "translate(" + -1*margin.left + "," + height/2 + ")")

///////////////////////////
// Step 4: Load the data //
///////////////////////////

// Load the data.
d3.json("../data/basic_chars_cleaned.csv", function(data) {

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
        return d3.schemeCategory10[colorScale(d.region)];
      })
      .sort(order)

  ///////////////////////////////////
  // Step 5: Add fluff and overlay //
  ///////////////////////////////////

  // Add a title.


  dot.append("title")
    .text(function(d) {
      return d.name;
    })


  // var box = yearLabel.node().getBBox();

  // var overlay = svg.append("rect")
  //     .attr("class", "overlay")
  //     .attr("x", box.x)
  //     .attr("y", box.y )
  //     .attr("width", box.width)
  //     .attr("height", box.height)
  //     .attr("transform", "translate(" + (height + margin.right*2) + "," + (height - margin.bottom) + ")")
  //     .on("mouseover", enableInteraction);


  // Defines a sort order so that the smallest dots are drawn on top.
  // function order(a, b) {
  //   return radius(b) - radius(a);
  // }

  function x(d) {
    // Return nation's income
    return d.lat;
  }
  function y(d) {
      // Return nation's lifeExpectancy
      return d.long;
  }
  function radius(d) {
      // Return nation's population
      return 3;
  }
  function color(d) {
      // Return nation's region
      return d.charter;
  }
  function key(d) {
      // Return nation's name
      return d.name;
  }

  //courtesy of http://techslides.com/convert-csv-to-json-in-javascript

  function csvJSON(csv){

    var lines=csv.split("\n");

    var result = [];

    var headers=lines[0].split(",");

    for(var i=1;i<lines.length;i++){

      var obj = {};
      var currentline=lines[i].split(",");

      for(var j=0;j<headers.length;j++){
        obj[headers[j]] = currentline[j];
      }

      result.push(obj);

    }
  
  //return result; //JavaScript object
  return JSON.stringify(result); //JSON
}

});
