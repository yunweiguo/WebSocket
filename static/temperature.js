/**
 * Created by yunweiguo on 26/02/2017.
 */
$(document).ready(function () {
    var _this ;
    $('.modify').click(function () {
        var $parent = $(this).parent().parent();
        var id = $parent.find(".equipment_id").html();

        $this = $(".item_" + id);
        _this = $this;

        $('.mod').show()

    })

    $(".confirm").click(function () {
        var v = $(".inp1").val();
        var equipment_id = $this.find(".equipment_id").html()
        _this.find(".temperature").html(v)

        $(".inp1").val("")
        $('.mod').hide()

        $.ajax({
             type: 'POST',
             url: "/temperature",
             data : {
                 "id": equipment_id,
                 "temperature": v
             },
        })

    })
})