/**
 * Created by yunweiguo on 26/02/2017.
 */
$(document).ready(function () {
    var _this ;

    $('.modify').click(function () {
        console.log($(this))
        var $parent = $(this).parent();console.log($parent)

        var id = $parent.find(".equipment_id").html();

        $this = $(".item_" + id);
        _this = $this;

        $('.mod').show()
        $('.mod').find(".equipment_id").html(id)

    })

    $(".confirm").click(function () {
        var v = $(".inp1").val();
        var equipment_id = $this.find(".equipment_id").html()

        _this.find(".smokescope").html(v)

        $(".inp1").val("")
        $('.mod').hide()

        $.ajax({
             type: 'POST',
             url: "/smoke",
             data : {
                 "id": equipment_id,
                 "smokescope": v
             },
        })

    })
})