'use strict';

console.log('Loading function');

exports.handler = (event, context, callback) => {
	console.log('Learning Lambda!!!');
	callback(null, "Hello World! from Lambda AWS.");
};

//This simple javascript returns Hello World! to the requester.
//Does nothing else.
//
//Method handler is responsible to catch requests to the Lambda function. Then the code within is executed.
//
//Callback parameter-function returns the Hello World string to the requester.
//
