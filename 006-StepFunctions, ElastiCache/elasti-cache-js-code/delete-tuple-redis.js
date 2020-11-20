var redis = require('redis');
var redisClient = redis.createClient({ host: 'my-redis-cluster.hwzwnc.ng.0001.use1.cache.amazonaws.com', port: 6379 });

redisClient.on('ready', function () {
    console.log("Redis is ready");
});

redisClient.on('error', function () {
    console.log("Error in Redis");
});

redisClient.del('age', function(err, reply) {
    console.log(reply);
});