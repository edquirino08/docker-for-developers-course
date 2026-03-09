const express = require("express");
const router = express.Router();
const userRepository = require("../database/user/user.repository");

router.get("/", async (req, res) => {
  const data = await userRepository.findAll();
  res.send(data);
});

module.exports = router;
