const express = require("express");
const app = express();

app.listen(3000, () => {
  console.log("Application started and Listening on port 3000");
});

app.use('/js', express.static('js'));

app.get("/", (req, res) => {
  res.sendFile("/html/podio_auth.html", {root: './'});
});