var express = require('express');
var router = express.Router();
var mongoose = require('mongoose')
var Post = mongoose.model('Post')
var	session	=	require('express-session');
var	passport	=	require('passport');
var	auth	=	require('./auth')(passport);
router.route('/posts')
	.get(
		function(req,res){
		Post.find({},	function(err,	posts){
		if(err)
				return	res.send(err);
		return	res.json({'posts'	:	posts});
		});
								})
	.post(
		function(req,res){
			post	=	new	Post()
			post.message	=	req.body.created_by;
			post.text	=	req.body.text;
			post.save(function(err,	post){
			if(err)
				res.send(err);
				res.json(post);
				});
		});
module.exports	= router;
