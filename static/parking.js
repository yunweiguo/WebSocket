/**
 * Created by yunweiguo on 14/02/2017.
 */
$(document).ready(function () {

    if("WebSocket" in window){
        ws = new WebSocket("ws://" + document.domain + ":7000/parking");
        ws.onopen = function () {
            alert("已经建立websocket连接")
        }
        ws.onmessage = function (msg) {
            var message = JSON.parse(msg.data);
            var id = message.id;
            var state = message.state;
            var start_time = message.start_time;
            var $this = $( ".item_" + id);
            $this.find(".state").html(state);
            $this.find(".start_time").html(start_time);
            if (state == "busy"){
                $this.find(".entry").attr("disabled", true);
                $this.find(".exit").attr("disabled", false);
            }else{
                $this.find(".entry").attr("disabled", false);
                $this.find(".exit").attr("disabled", true);
            }
        }

        $(".entry").click(function () {
            var $parent = $(this).parent().parent();
            var id = $parent.find(".parking_id").html();
            var state = "busy"
            var msg = {"id": id, "state": state}
            ws.send(JSON.stringify(msg))
         })
        $(".exit").click(function () {
            var $parent = $(this).parent().parent();
            var id = $parent.find(".parking_id").html();
            var state = "available"
            var msg = {"id": id, "state": state}
            ws.send(JSON.stringify(msg))
         })
    }
    else{
        alert("不支持websocket协议")
    }


})



