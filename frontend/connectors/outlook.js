window.outlookConnector = {
  connect: function() { console.log("Outlook connect [placeholder]"); },
  disconnect: function() { console.log("Outlook disconnect"); },
  send: function(msg) { console.log("Outlook send:", msg); },
  onMessage: function(callback) { console.log("Outlook onMessage registered"); }
};
