var i = 0;
function updateCurrent(){ 
    var getCurrent = $.getJSON("/api/current", function(result){
        console.log(result);
        $("#currentTemp").html(result.temp); 
        $("#currentHumidity").html(result.humidity);
        $("#currentDate").html(moment(result.date).tz("America/New_York").calendar());
        $("#noConnection").hide();
        i = i + 1;
        console.log("Update " + i);
    });
    getCurrent.fail(function(){
        $("#noConnection").show(); 
    });
};
updateCurrent();
$(document).ready(function(){
    window.setInterval(updateCurrent, 60000);
});

