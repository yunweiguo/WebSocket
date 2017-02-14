/**
 * Created by yunweiguo on 14/02/2017.
 */
$(document).ready(function () {

    if("WebSocket" in window){
        ws = new WebSocket("ws://" + document.domain + ":7000/alarm");
        ws.onopen = function () {
            alert("已经建立websocket连接")
        }
        ws.onmessage = function (msg) {
            var message = JSON.parse(msg.data);
            var id = message.id;
            var state = message.state;
            var $this = $( ".item_" + id);
            $this.find(".state").html(state);
            if (state == "on"){
                $this.find(".on").attr("disabled", true);
                $this.find(".off").attr("disabled", false);
            }else{
                $this.find(".on").attr("disabled", false);
                $this.find(".off").attr("disabled", true);
            }
        }
        $(".on").click(function () {
            var $parent = $(this).parent().parent();
            var id = $parent.find(".alarm_id").html();
            var state = "on"
            var msg = {"id": id, "state": state}
            ws.send(JSON.stringify(msg))
         })
        $(".off").click(function () {
            var $parent = $(this).parent().parent();
            var id = $parent.find(".alarm_id").html();
            var state = "off"
            var msg = {"id": id, "state": state}
            ws.send(JSON.stringify(msg))
         })
    }
    else{
        alert("不支持websocket协议")
    }


})



