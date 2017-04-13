/**
 * Created by yunweiguo on 26/02/2017.
 */
$(document).ready(function () {

    $(".on").click(function () {

        var $parent = $(this).parent().parent();
        var id = $parent.find(".equipment_id").html();
        var state = 'on';
        var $this = $( ".item_" + id);


        $.ajax({
             type: 'POST',
             url: "/manual",
             data : {
                 "id": id,
                 "state": "on"
             },
             success: function (data) {
                $this.find(".on").attr("disabled", true);
                $this.find(".off").attr("disabled", false);
                $this.find(".state").html("on")
             }
        })
    })
    $(".off").click(function (data) {

        var $parent = $(this).parent().parent();
        var id = $parent.find(".equipment_id").html();
        var state = 'on';
        var $this = $( ".item_" + id);

        $.ajax({
             type: 'POST',
             url: "/manual",
             data : {
                 "id": id,
                 "state": "off"
             },
            success: function () {
                $this.find(".on").attr("disabled", false);
                $this.find(".off").attr("disabled", true);
                $this.find(".state").html("off")
            }
        })
    })

})