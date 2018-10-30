//	otherfile.js
var	mongoose	=	require(	'mongoose'	);
var	Post	=	mongoose.model('Post');
Post.findById(id,	function(err,	post){})
Post.find({},	function(err,	posts){
		console.log(posts)
})