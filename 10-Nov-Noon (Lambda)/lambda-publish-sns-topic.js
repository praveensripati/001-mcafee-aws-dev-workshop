console.log("Loading function");

var AWS = require("aws-sdk");

exports.handler = function (event, context) {
	var eventText = JSON.stringify(event, null, 2);

	console.log("Received event:", eventText);

	var sns = new AWS.SNS();

	var params = {
		Message: "An object is added in SQS",

		Subject: "Message from SNS",

		TopicArn: "arn:aws:sns:us-east-1:1234567890:MyDemoTopic" //Give the ARN of your SNS
	};

	sns.publish(params, context.done);

	console.log("Published messages to SNS Topic");

};