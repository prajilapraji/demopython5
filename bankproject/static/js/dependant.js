$(document).ready(function() {
    $("#district").change(function() {
        var district_id = $(this).val();
        var url = "/get-states/?district_id="+district_id;
        $.get(url, function(data, status){
            $("#branch").html(data);
        });
    });
});

