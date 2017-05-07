/////////////////////////////////////
// Some code copied from d3 project//
/////////////////////////////////////

// zooming courtesy of:
// https://bl.ocks.org/mbostock/db6b4335bf1662b413e7968910104f0f

// csv inner join courtesy of:
// http://stackoverflow.com/questions/17500312/is-there-some-way-i-can-join-the-contents-of-two-javascript-arrays-much-like-i/17500836#17500836

$( document ).ready(function() {

    // Chart dimensions
    var margin = {top: 19.5, right: 19.5, bottom: 19.5, left: 39.5};
    var width = 960 - margin.right;
    var height = 500 - margin.top - margin.bottom;
    var startColor = '#ff0000';
    var endColor = '#00ff00';

    // Various scales
    var xScale = d3.scaleLinear().domain([-73514, -69988]).range([0, width]),
        yScale = d3.scaleLinear().domain([41244, 42871]).range([height, 0]),
        colorScale = d3.scaleLinear().domain([0, 10]).range([startColor, endColor]);
        colorScale2 = d3.scaleOrdinal([0,1]);

    // The x & y axes
    var xAxis = d3.axisBottom(xScale),
        yAxis = d3.axisLeft(yScale);

    var level = d3.select("#level span"),
        town = d3.select("#town span"),
        charter_stat = d3.select("#charter_stat span")
        school_name = d3.select("#school_name span");


    // Load the data.
    d3.csv("basic_chars.csv", function(locations) {

      d3.csv("success_metric.csv", function(successes) {

        var data = innerJoin(locations, successes, function(location, success) {
          if (location.year === success.year && location.school_id === success.school_id) {  
            return {
                id: location.school_id,
                name: location.school,
                year: location.year,
                charter: location.charter,
                level: location.level,
                town: location.town,
                lat: location.lat,
                long: location.long,
                success: success.success,
                ela_success: success.ela_success,
                math_success: success.math_success
                };
          };
        })

        data = data.filter(function(d) {
          // we're only using one year for now
          return d.year == 2013;
        })


        var svg = d3.select("#chart").append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
          .append("g")
          .attr("transform", "translate(" + margin.left + "," + 0 + ")");
            
        var dot = svg.append("g")
            .attr("class", "dots")
          .selectAll("class", "dot")
            .data(data)
          .enter()
            .append("circle")
            .attr("class", "dot")
            .call(position)
            .attr("fill", function(d) {
             // return d3.schemeCategory10[colorScale(color(d))];
             return colorScale(color(d));
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

        d3.select("#success")
            .on("click", function(d,i) {
                dot.data(data)
                  .attr("fill", function(d) {
                    return colorScale(color(d));
                  })
            })
        d3.select("#charter")
            .on("click", function(d,i) {
                dot.data(data)
                  .attr("fill", function(d) {
                    return d3.schemeCategory10[colorScale2(d.charter)];
                  })
            })
        d3.select("#math")
            .on("click", function(d,i) {
                dot.data(data)
                  .attr("fill", function(d) {
                    return colorScale(d.math_success);
                  })
            })
        d3.select("#english")
            .on("click", function(d,i) {
                dot.attr("fill", function(d) {
                    return colorScale(d.ela_success);
                  })
            })

        // Add a title.


        dot.append("title")
          .text(function(d) {
            return d.name;
          })

        dot.on("mouseover", function(d) {
          level.text(d.level)
          town.text(d.town)
          charter_stat.text(d.charter)
          school_name.text(d.name)
        })

        dot.on("click", function(d){
          getNeighbors(d);

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
            return d.success;
        }
        function key(d) {
            // Return school's name
            return d.name;
        }

        svg.call(zoom);

        function position(dot) {
          dot.attr("cx", function(d) {
            return xScale(x(d)); })
              .attr("cy", function(d) { return yScale(y(d)); })
              .attr("r", function(d) { return radius(d); });
        }

        function innerJoin(a, b, select) {
          var m = a.length, n = b.length, c = [];

          for (var i = 0; i < m; i++) {
              var x = a[i];

              for (var j = 0; j < n; j++) { // cartesian product - all combinations
                  var y = select(x, b[j]);  // filter out the rows and columns you want
                  if (y) c.push(y);         // if a row is returned add it to the table
              }
          }

          return c;
        }
      })
    });
});


function getNeighbors(school) {

  var school_id = +school.id;
  var year = +school.year;
  getNeighborsRequest(school_id, year);

}

function showNeighbors(results, school_id) {

  var data = results;
  console.log(data);
  console.log(school_id);

  var width = 800,
  barHeight = 20;

  var x = d3.scaleLinear()
      .range([0, 450]);

  var xAxis = d3.axisBottom(x);

  //clear the previous graph
  var chart_selector = $(".graph");
  chart_selector.empty()

  var chart = d3.select(".graph")
      .attr("width", width);
  
  data.forEach(function(d){
    d.id = +d.school_id;
    d.success = +d.success;
    d.year = +d.year;
    d.name = d.school;
  });

  x.domain([0, d3.max(data, function(d) { return d.success; })]);

  data.sort(function (a, b) {
      return b.success - a.success;
  });

  chart.attr("height", barHeight * data.length);

  var bar = chart.selectAll("g")
      .data(data)
  .enter().append("g")
      .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });

  var x_axis = chart.append('g')
      .attr("transform", "translate(150,220)")
      .attr('id','xaxis')
      .call(xAxis);

  bar.append("text")
      .attr("x", 235)
      .attr("y", barHeight / 2)
      .attr("text-anchor", "end")
      .attr("dy", ".35em")
      .text(function(d) { 
          return d.name + "  "});
      
  bar.append("rect")
      .attr("x", 240)
      .attr("width", function(d) { 
          return x(d.success); })
      .attr("height", barHeight - 2)
      .attr("fill", function(d){ 
          if (d.id == school_id){
            return "palegreen";
          } 
          else{ 
            return "darkslategray";}})

  bar.append("text")
      .attr("x", function(d) { return x(d.success) + 275})
      .attr("y", barHeight / 2)
      .attr("dy", ".35em")
      .attr("text-anchor", "end")
      .text(function(d) { 
          return d.success; });

  bar.on("click", function(d){
      getNeighbors(d);
    })
}

function getNeighborsRequest(school_id, year) {

  $.get('/neighbors.json', { id: school_id, y: year }, function(res){
        getNeighborsInfoRequest(res, school_id);
    });
}

function getNeighborsInfoRequest(res, school_id) {
  console.log(res);

  $.get('/neighbors_info.json', res[0], function(res){
        showNeighbors(res, school_id);
    });
}







