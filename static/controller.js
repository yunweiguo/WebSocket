/**
 * Created by yunweiguo on 14/02/2017.
 */
$(document).ready(function () {

    initDynamic();
    initParking();

    if("WebSocket" in window){
        ws = new WebSocket("ws://" + document.domain + ":7000/ws/controller");
        ws.onopen = function () {
            alert("已经建立websocket连接");
        }
        ws.onmessage = function (msg) {
            var message = JSON.parse(msg.data);
            var msg_type = message.msg_type;
            if (msg_type == 'history'){
                var history_list = msg.data;

            }else if (msg_type == "update"){
                var update_info = msg.data;
            }

        }


        $(".history").click(function () {
            var $parent = $(this).parent().parent();
            var id = $parent.find(".id")
            ws.send(JSON.stringify({"id": id}))
        })
    }
    else{
        alert("不支持websocket协议")
    }



})


function initDynamic() {
    $.ajax({
        type: 'GET',
        url: "/dynamic",
        success: function (data) {
            $(".dynamic_tbody").html("");
            var body = "";
            var res = JSON.parse(data);
            if (res['is_succ']){
                var items = res['data'];
                for (var i =0; i<items.length; i++){
                    var id = items[i]['id'];
                    var type = items[i]['type'];
                    var device_name = items[i]['device_name'];

                    var temperature;
                    if (type == "temperature"){
                        temperature = items[i]['temperature'];
                    }else{
                        temperature = "--"
                    }

                    var smokescope;
                    if (type == "smoke"){
                        smokescope = items[i]['smokescope'];
                    }else{
                        smokescope = "--"
                    }

                    body += "<tr>"
                        + "<td class='id' hidden>" + id + "</td>"
                        + "<td class='name'>" + device_name +  "</td>"
                        + "<td class='smoke'>" + smokescope + "</td>"
                        + "<td class='temperature'>" + temperature +"</td>"
                        + "<td class='operation'><button class='history btn btn-default'>历史记录</button></td>"
                        + "</tr>";
                }

                $(".dynamic_tbody").html(body);
            }
        }
    })
}



function initParking() {
    $.ajax({
        type: 'GET',
        url: "/parking",
        success: function (data) {
            $(".parking_tbody").html("");
            var body = "";
            var res = JSON.parse(data);
            if (res['is_succ']){
                var items = res['data'];
                for (var i =0; i<items.length; i++){
                    var id = items[i]['id'];
                    var state = items[i]['state'];
                    var device_name = items[i]['device_name'];

                    var button_html = "";

                    body += "<tr>"
                        + "<td class='id' hidden>" + id + "</td>"
                        + "<td class='name'>" + device_name +  "</td>"
                        + "<td class='state'>" + state + "</td>"
                        + "<td class='operation'><button class='history btn btn-default'>历史记录</button></td>"
                        + "</tr>";
                }

                $(".parking_tbody").html(body);
            }
        }
    })
}