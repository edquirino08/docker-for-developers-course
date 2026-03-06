const { MongoClient } = require("mongodb");

const uri = process.env.MONGO_URI;

console.log(uri);

const connectDB = async () => {
  const client = new MongoClient(uri);

  try {
    await client.connect();
    console.log("Conectado ao MongoDB");
    return client;
  } catch (error) {
    console.error("Erro ao conectar ao MongoDB:", error);
    process.exit(1);
  }
};

module.exports = connectDB;