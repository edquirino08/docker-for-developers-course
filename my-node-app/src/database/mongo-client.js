const mongoose = require("mongoose");
require("dotenv").config();

const uri = process.env.MONGO_URI;

async function connectMongoDB() {
  try {
    await mongoose.connect(uri);
    console.log("MongoDB Connected");
  } catch (err) {
    console.log("MongoDB Connection Error:", err);
  }
}

module.exports = connectMongoDB;