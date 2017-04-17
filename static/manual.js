/**
 * Created by yunweiguo on 26/02/2017.
 */
$(document).ready(function () {

    init();

    $("table").delegate(".on", "click", function () {

        var $parent = $(this).parent().parent();
        var id = $parent.find(".id").html();
        var device_name = $parent.find(".name").html();
        var state = 'on';

        $.ajax({
             type: 'POST',
             url: "/manual",
             data : {
                 "type": "manual",
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
        var state = 'off';

        $.ajax({
             type: 'POST',
             url: "/manual",
             data : {
                 "type": "manual",
                 "id": id,
                 "state": state,
                 "device_name": device_name,
             },
             success: function (data) {
                init();
             }
        })
    })

})


function init() {
    $.ajax({
        type: 'GET',
        url: "/manual",
        success: function (data) {
            $(".tbody").html("");
            var body = "";
            var res = JSON.parse(data);
            if (res['is_succ']){
                var items = res['data'];
                console.info(items)
                for (var i =0; i<items.length; i++){
                    var id = items[i]['id'];
                    var state_ = items[i]['state'];
                    var state;
                    var device_name = items[i]['device_name'];
                    var type = items[i]['type'];
                    var button_html = "";
                    if (state_ == 'on') {
                        state = "报警中"
                        button_html = "<button class='off btn btn-default'>停止</button>"
                            + "<button class='on btn btn-default' disabled='disabled'>报警</button>";
                    } else if (state_ == 'off') {
                        state = "正常"
                        button_html = "<button class='off btn btn-default' disabled='disabled'>停止</button>"
                            + "<button class='on btn btn-default'>报警</button>";
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