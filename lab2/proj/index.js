var	express	=	require('express');
require('./models/post');
var	app	=	express();
var	bodyParser	=	require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({	extended:	false	}));
var	api	=	require('./routes/api');

app.use('/api',	api);
module.exports	=	app;
