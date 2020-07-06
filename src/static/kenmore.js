$(document).ready(function() {
  $("#mode_off").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/mode", {"data": "off"});
  });
  $("#mode_cool").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/mode", {"data": "cool"});
  });
  $("#mode_save").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/mode", {"data": "energy_saver"});
  });
  $("#mode_fan").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/mode", {"data": "fan_only"});
  });

  $("#fan_low").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/fan", {"data": "1"});
  });
  $("#fan_med").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/fan", {"data": "2"});
  });
  $("#fan_high").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/fan", {"data": "3"});
  });
  $("#fan_auto").click(function(){
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/fan", {"data": "auto"});
  });
});
