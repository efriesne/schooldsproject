

/////// README
// call plotConfusionMatrix as shown below
// true positives are underlined, change startColor and endColor to change color gradient
//////


ratioMatrix = 
[[  0,   0,   0,   0,   0,   1,   0,   0],
 [  0,   0,   0,   2,   0,   2,   0,   0],
 [  0,   0,   0,   4,   2,  46,   0,   0,],
 [  0,   0,   0,   0,   0, 164,   0,   0,],
 [  0,   0,   0,   3,   1, 332,   0,   0,],
 [  0,   0,   0,   0,   1, 414,   0,   0,],
 [  0,   0,   0,   0,   1, 260,   0,   0,],
 [  0,   0,   0,   0,   0,  51,   0,   0,]]

 licensedMatrix =
 [[  0,   0,   0,   0,   0,   1,   0,   0,],
 [  0,   0,   0,   0,   0,   4,   0,   0,],
 [  0,   0,   0,   0,   0,  52,   0,   0,],
 [  0,   0,   0,   0,   0, 164,   0,   0,],
 [  0,   0,   0,   0,   0, 336,  0,   0,],
 [  0,   0,   0,   0,   0, 415,   0,   0,],
 [  0,   0,   0,   0,   0, 261,   0,   0,],
 [  0,   0,   0,   0,   0,  51,   0,   0]]

 qualifiedMatrix = 
 [[  0,   0,   0,   0,   1,   0,   0,   0,],
 [  0,   0,   0,   2,   0,   2,   0,   0,],
 [  0,   0,   2,  10,   2,  38,   0,   0,],
 [  0,   0,   0,  19,   8, 137,   0,   0,],
 [  0,   0,   5,  13,   9, 309,   0,   0,],
 [  0,   0,   1,  15,   7, 392,   0,   0,],
 [  0,   0,   1,   1,   2, 257,   0,   0,],
 [  0,   0,   0,   1,   0,  50,   0,   0,]]

 allMatrix = 
 [[  0,   0,   0,   1,   0,   0,   0,   0,],
 [  0,   0,   0,   2,   1,   1,   0,   0,],
 [  0,   0,   2,   9,  15,  26,   0,   0,],
 [  0,   0,   0,  15,  34, 115,   0,   0,],
 [  0,   1,   0,  11,  53, 271,   0,   0,],
 [  0,   0,   0,  13,  31, 369,   2,   0,],
 [  0,   0,   1,   1,  15, 243,   1,   0,],
 [  0,   0,   0,   0,   0,  51,   0,   0,]]

 incidentMatrix = 
 [[  0,   0,   0,   0,   0,   0,   0,],
 [  1,  10,  48,  24,  28,   8,   0,],
 [  1,  16, 554,  90,  52,  32,   0,],
 [  0,   8, 131,  81,  33,  22,   0,],
 [  3,   8, 211,  57,  99,  48,   0,],
 [  3,  13, 226,  41,  70,  89,   0,],
 [  0,   1,  11,   3,   7,   2,   0,]]



incidentLabels = ["3-4","4-5","5-6","6-7","7-8","8-9","9-10"]
plotConfusionMatrix(incidentMatrix, 0, 554, incidentLabels);



// minVal = min val in the matrix
// maxVal = max val in the matrix
function plotConfusionMatrix(matrix, minVal, maxVal, labels) {

// Chart dimensions
var margin = {top: 19.5, right: 19.5, bottom: 19.5, left: 39.5};
var width = 400
var height = 400
var numRows = matrix.length;
var numCols = matrix[0].length;
var startColor = '#ffffff'
var endColor = '#1062ed'

// Various scales
var xScale = d3.scaleBand().domain(d3.range(numCols)).range([0, width]),
    yScale = d3.scaleBand().domain(d3.range(numRows)).range([0, height]),
    colorScale = d3.scaleLinear().domain([minVal, maxVal]).range([startColor, endColor]);
console.log(xScale.bandwidth())


// Create the SVG container and set the origin
var svg = d3.select("#chart").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
var border = svg.append("rect")
      .style("stroke", "black")
      .style("stroke-width", "2px")
      .style("fill", "none")
      .attr("width", width)
      .attr("height", height);

//////////////////////////////////////
// Add axis  labels //
//////////////////////////////////////
xLabel = svg.append("text")
    .attr("class", "label")
    .attr("id", "xlabel")
    .text("predicted success metric (3-10)")
    .attr("transform", "translate("+ width + "," + (height-5) + ")")
    .attr("text-anchor", "end");
yLabel = svg.append("text")
    .attr("class", "label")
    .attr("id", "ylabel")
    .text("actual success metric (3-10)")
    .attr("transform", "rotate(-90)")
    .attr("y", 10)
    .attr("text-anchor", "end");


var row = svg.selectAll("g")
      .data(matrix)
      .enter()
      .append("g")
      .attr("class", "row")
      .attr("id", function(d,i) { return i})
      .attr("transform", function(d, i) { return "translate(0," + yScale(i) + ")"; });

var overlay = svg.append("g");

var actualLabels = overlay.selectAll("g")
      .data(labels)
      .enter().append("g")
      .attr("transform", function(d, i) { return "translate(" + 0 + "," + yScale(i) + ")"; })
      .append("text")
      .attr("x", -12)
      .attr("y", yScale.bandwidth() / 2)
      .style("font-size", "12px")
      .style("font-weight", "bold")
      .attr("text-anchor", "end")
      .text(function(d) { return d; });
var predictLabels = overlay.selectAll(".predictlabels")
    .data(labels)
    .enter()
    .append("g")
    .attr("transform", function(d, i) { return "translate(" + xScale(i) + "," + 0 + ")"; })
    .append("text")
      .attr("x", xScale.bandwidth() / 2)
      .attr("y", -11)
      .attr("text-anchor", "end")
      .style("font-size", "12px")
      .style("font-weight", "bold")
      .text(function(d) { return d; });


var cell = row.selectAll("g")
      .data(function(d) { return d; })
      .enter()
      .append("g")
      .attr("class", "cell")
cell.append("rect")
      .attr("width", xScale.bandwidth())
      .attr("height", yScale.bandwidth())
      .attr("stroke", "#eff3f9")
      .attr("fill", function(d) {
       return colorScale(d)})
      .attr("transform", function(d, i) { return "translate(" + xScale(i) + "," + 0 + ")"; })
cell.append("text")
  .attr("x", function(d, i) { return xScale(i)+(xScale.bandwidth()/2); })
  .attr("y", yScale.bandwidth()/2)
  .style("font-size", "13px")
  .attr("text-anchor", "middle")
  .attr("text-decoration", function(d,i){
    row = parseInt(this.parentElement.parentElement.id);
    return row == i ? 'underline' : 'none'
  })
  .style("font-size", function(d,i){
    row = parseInt(this.parentElement.parentElement.id);
    return row == i ? '17px' : '12px'
  })
  .style("fill", function(d, i) { return d > 1 ? 'black' : startColor; })
  .text(function(d) { return d; });


}
