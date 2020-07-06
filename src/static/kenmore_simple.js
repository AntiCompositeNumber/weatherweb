$(document).ready(function() {
  $("#btn_pwr").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/power");
  });
  $("#btn_timer").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/timer");
  });
  $("#btn_fan_up").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/fan_up");
  });
  $("#btn_fan_down").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/fan_down");
  });
  $("#btn_temp_up").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/temp_up");
  });
  $("#btn_temp_down").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/temp_down");
  });
  $("#btn_cool").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/cool");
  });
  $("#btn_save").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/energy_saver");
  });
  $("#btn_fan").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/fan_only");
  });
  $("#btn_auto_fan").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/auto_fan");
  });
  $("#btn_sleep").click(function() {
    $.post($SCRIPT_ROOT + "/api/v1/device/kenmore/simple/sleep");
  });
});
