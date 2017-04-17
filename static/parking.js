/**
 * Created by yunweiguo on 06/04/2017.
 */
$(document).ready(function () {

    init();

    $("table").delegate(".on", "click", function () {
        var $parent = $(this).parent().parent();
        var id = $parent.find(".id").html();
        var device_name = $parent.find(".name").html();
        var state = 'busy';

        $.ajax({
             type: 'POST',
             url: "/parking",
             data : {
                 "type": "parking",
                 "id": id,
                 "state": state,
                 "device_name": device_name,
             },
             success: function (data) {
                init();
             }
        })
    })



    $("table").delegate(".off", "click", function () {
        var $parent = $(this).parent().parent();
        var id = $parent.find(".id").html();
        var device_name = $parent.find(".name").html();
        var state = 'available';

        $.ajax({
             type: 'POST',
             url: "/parking",
             data : {
                 "type": "parking",
                 "id": id,
                 "state": state,
                 "device_name": device_name,
             },
            success: function () {
                init();
            }
        })
    })

    $("table").delegate(".enter", "click", function () {

    })


})

function init() {
    $.ajax({
        type: 'GET',
        url: "/parking",
        success: function (data) {
            $(".tbody").html("");
            var body = "";
            var res = JSON.parse(data);
            if (res['is_succ']){
                var items = res['data'];
                console.info(items)
                for (var i =0; i<items.length; i++){
                    var id = items[i]['id'];
                    var state ;
                    var device_name = items[i]['device_name'];
                    var type = items[i]['type'];
                    var button_html = "";
                    if (type == 'parking'){
                        state = items[i]['state'];
                        if (state == 'available') {
                            button_html = "<button class='on btn btn-default'>停车</button>"
                                + "<button class='off btn btn-default' disabled='disabled'>离开</button>";
                        } else if (state == 'busy'){
                            button_html = "<button class='on btn btn-default' disabled='disabled'>停车</button>"
                                + "<button class='off btn btn-default'>离开</button>";
                        }
                    }else if (type == 'entrance') {
                        state = '--'
                        button_html = "<button class='enter btn btn-default'>进入停车场</button>"
                                + "<button class='left btn btn-default'>离开停车场</button>";
                    }



                    body += "<tr>"
                        + "<td class='id' hidden>" + id + "</td>"
                        + "<td class='name'>" + device_name +  "</td>"
                        + "<td class='state'>" + state + "</td>"
                        + "<td class='operation'>" + button_html +"</td>"
                        + "</tr>";
                }

                $(".tbody").html(body);
            }
        }
    })
}