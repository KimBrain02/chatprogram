// 통신관련함수
module.exports = function(io) {
    //io~~~~
    io.on("connection",async(socket)=>{
        console.log("client is connected", socket.id);
    });
};