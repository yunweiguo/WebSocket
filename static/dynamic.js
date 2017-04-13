/**
 * Created by yunweiguo on 07/04/2017.
 */

$(document).ready(function () {

    init();

    $("table").delegate(".modify", "click", function () {
        alert('hh')
    })



})

function init() {
    $.ajax({
        type: 'GET',
        url: "/dynamic",
        success: function (data) {
            $(".tbody").html("");
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
                        + "<td class='operation'><button class='modify btn btn-default'>修改</button></td>"
                        + "</tr>";
                }

                $(".tbody").html(body);


            }
        }
    })


}