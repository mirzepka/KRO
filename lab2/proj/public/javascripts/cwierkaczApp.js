var	app	=	angular.module('cwierkaczApp',	[]);
app.controller('mainController',	function($scope){
		$scope.posts	=	[];	//	wszystkie	wpisy
		$scope.newPost	=	{created_by:	'',	text:	'',	created_at:	''};	//	dane	formularza
		$scope.post	=	function(){
				$scope.newPost.created_at	=	Date.now();	//	data	utworzenia
				$scope.posts.push($scope.newPost);	//	dodaj	wpis	do	widoku
				$scope.newPost	=	{created_by:	'',	text:	'',	created_at:	''};	//	czyść	formularz
		};
});

app.use(session({secret:	'secret	token'}));
app.use(passport.initialize());
app.use(passport.session());
var	initPassport	=	require('./config/passport-init');
initPassport(passport);
app.use('/auth',	auth);