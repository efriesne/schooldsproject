var express = require('express')
var bodyParser = require('body-parser');
var anyDB = require('any-db');
var engines = require('consolidate');
var path = require('path');

var app = express();


//Setting up hogan
//app.engine('html', engines.hogan); 
//app.set('views', __dirname + '/views');
//app.set('view engine', 'html'); 

//CSS and JS files
//app.use(express.static(path.join(__dirname, 'public')));

app.use(bodyParser.urlencoded({extended:false}));
app.use(bodyParser.json());

var conn = anyDB.createConnection('school_data.db');



//Request for home page
app.get('/', function(request, response) {
	console.log('Homepage requested');
	response.render('map.html');
});

app.get('/neighbors', saveMessage);

function nearestNeighbors(request, response) {
  	var select_terms = request.params.select;   

	var query = "SELECT * FROM success WHERE schoold_id=$1";	
	conn.query(query, [id], function(error, data) {
		if (error != null){
			console.log(error);
		}
		else{
			console.log();
		}

		response.end('Successfully nearest neighbor!');
	});
}

//Start listening on port
app.listen(8080, function(error, response) {
	if (error != null){
		console.log("Error: " + error);
	}
	else {
		console.log('listening on port: 8080');
	}
});




