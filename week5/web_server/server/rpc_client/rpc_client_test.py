
var client = require('./rpc_client');

// invoke 'add'
client.add(1, 2, function(result) {
  console.assert(result === 3);
});