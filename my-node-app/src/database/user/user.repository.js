const User = require("../user/user.entity");

async function findAll() {
  return User.find(); 
}

module.exports = { findAll };
