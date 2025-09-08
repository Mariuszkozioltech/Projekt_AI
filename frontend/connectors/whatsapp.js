window.whatsappConnector = {
  connect: function() { console.log("WhatsApp connect [placeholder]"); },
  disconnect: function() { console.log("WhatsApp disconnect"); },
  send: function(msg) { console.log("WhatsApp send:", msg); },
  onMessage: function(callback) { console.log("WhatsApp onMessage registered"); }
};
