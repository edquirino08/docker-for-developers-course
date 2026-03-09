const express = require("express");
const connectMongoDB = require("./src/database/mongo-client");
const userRoutes = require("./src/routes/user.routes");

const app = express();
const PORT = 3000;

app.use("/user", userRoutes);

app.listen(PORT, () => {
  console.log(`Servidor rodando em http://localhost:${PORT}`);
});

connectMongoDB();
