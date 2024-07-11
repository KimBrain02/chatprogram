const mongoose = require("mongoose")

//Schema는 설계도
const userSchema = new mongoose.Schema({
    
    name: {
        type: String,
        required: [true, "User must type name"],
        unique: true,
    },
    //연결 Id
    token: {
        type: String,
    },
    //온 오프라인인지 확인
    online: {
        type: Boolean,
        default: false,
    },
});
module.exports = mongoose.model("User", userSchema);