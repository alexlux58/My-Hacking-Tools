const http = require("http");
const WebSocketServer = require("websocket").server;
let connection = null;

const httpServer = http.createServer((req, res) => {
  console.log("we have received a request");
});

const websocket = new WebSocketServer({
  "httpServer": httpserver,
});

websocket.on("request", (request) => {
  request.accept(null, request.origin);
  connection.on("onopen", () => console.log("Opened"));
  connection.on("onclose", () => console.log("Closed"));
  connection.on("onmessage", () => (message) => {
    console.log(`Recieved: ${message}`);
  });
});

httpServer.listen(8080, () =>
  console.log("My server is listening on port 8080")
);
