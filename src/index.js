const express = require("express");
const app = express();
const port = 3000;

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});


app.post("/", (req, res) => {
  res.send("Hello world");
});
