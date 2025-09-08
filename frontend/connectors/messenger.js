window.messengerConnector = {
  connect: function() { console.log("Messenger connect [placeholder]"); },
  disconnect: function() { console.log("Messenger disconnect"); },
  send: function(msg) { console.log("Messenger send:", msg); },
  onMessage: function(callback) { console.log("Messenger onMessage registered"); }
};
