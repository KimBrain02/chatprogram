const express = require("express");
const mongoose = require("mongoose");
require("dotenv").config();
const cors = require("cors");

const app = express();
app.use(cors());
//데이터베이스 연결

mongoose.connect(process.env.DB, {
  }).then(()=>console.log("connected to databasse"));

module.exports=app