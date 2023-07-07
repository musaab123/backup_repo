odoo.define('portal_attendance.portal_attendance', function (require) {
    "use strict";
    // var core = require('web.core');
    // var Dialog = require("web.Dialog");
    // var session = require('web.session');
    var ajax = require('web.ajax');
    var Widget = require('web.Widget');
    var publicWidget = require('web.public.widget');
    // var websiteRootData = require('website.root');
    // var utils = require('web.utils');
    // var field_utils = require('web.field_utils');
    // var _t = core._t;
    // var qweb = core.qweb;
    var latitude = "";
    var longitude = "";
    window.location_data = "";
    // const time = require('web.time');
    // var currentUser = session.uid;
    
    publicWidget.registry.checkin_out_portal_page = publicWidget.Widget.extend({
        
        selector: '.js_chechin_out_data',
        events: {
            'click .checkin_btn': '_onClickChechInButton',
            'click .after_checkin_btn': '_onClickAfterChechInButton',
            'click .checkout_btn': '_onClickChechOutButton',
            'click .after_checkout_btn': '_onClickAfterChechOutButton',
        },
        async start() {
            await this._super(...arguments);

            var flag = $("input[name='flag']").val();
            if (flag == 1){
                $("div.checkin").hide();
                $("div.checkout").show();
                $("div.after_checkout").hide();
                $("div.after_checkin").hide();
            }
            else{
                $("div.checkin").show();
                $("div.checkout").hide();
                $("div.after_checkout").hide();
                $("div.after_checkin").hide();
            }
            
            if ("geolocation" in navigator) {
                navigator.geolocation.getCurrentPosition(setCurrentJSPosition, positionJSError, {
                    enableHighAccuracy: true,
                    timeout: 15000,
                    maximumAge: 0,
                });

                function setCurrentJSPosition(position) {
                    latitude = position.coords.latitude;
                    longitude = position.coords.longitude;
                }
                function positionJSError(error) {
                    switch (error.code) {
                        case error.PERMISSION_DENIED:
                            alert("User denied the request for Geolocation.");
                            return true; 
                        case error.POSITION_UNAVAILABLE:
                            alert("Location information is unavailable.");
                            return true; 
                        case error.TIMEOUT:
                            alert("The request to get user location timed out.");
                            return true;  
                        case error.UNKNOWN_ERROR:
                            alert("An unknown error occurred.");
                            return true;      
                    }
                }
            } else {
                console.log("API Not Supported.");
            }
        },


        async _onClickChechInButton() {
            var currentDate = new Date();
  
            var year = currentDate.getFullYear();
            var month = currentDate.getMonth() + 1; 
            var day = currentDate.getDate();
            
            var hours = currentDate.getHours();
            var minutes = currentDate.getMinutes();
            var seconds = currentDate.getSeconds();
            
            month = (month < 10 ? "0" : "") + month;
            day = (day < 10 ? "0" : "") + day;
            hours = (hours < 10 ? "0" : "") + hours;
            minutes = (minutes < 10 ? "0" : "") + minutes;
            seconds = (seconds < 10 ? "0" : "") + seconds;
            
            var currentDateTime = year + "/" + month + "/" + day + " " + hours + ":" + minutes + ":" + seconds;
            

            var message = $(".checkin_message").val();
            var employee_id = $("input[name='employee_id']").val();


            if(!latitude || !longitude){
                alert("Please Check your browser Settings and Allow Location !")
	        }else{
                var result = {}
                result['employee_id'] = employee_id
                result['message'] = message
                result['latitude'] = latitude
                result['longitude'] = longitude
                ajax.jsonRpc('/check/get_sh_attendance_manual', 'call', result).then( function(res){
                });
	        }

            var checkin_time = $("#checkin_time");
            checkin_time.text(""+currentDateTime+"");

            $("div.checkin").hide();
            $("div.checkout").hide();
            $("div.after_checkout").hide();
            $("div.after_checkin").show();
        },

        async _onClickAfterChechInButton() {
            $("div.checkin").hide();
            $("div.checkout").show();
            $("div.after_checkout").hide();
            $("div.after_checkin").hide();
        },

        async _onClickChechOutButton() {
            var currentDate = new Date();
  
            var year = currentDate.getFullYear();
            var month = currentDate.getMonth() + 1; 
            var day = currentDate.getDate();
            
            var hours = currentDate.getHours();
            var minutes = currentDate.getMinutes();
            var seconds = currentDate.getSeconds();
            
            month = (month < 10 ? "0" : "") + month;
            day = (day < 10 ? "0" : "") + day;
            hours = (hours < 10 ? "0" : "") + hours;
            minutes = (minutes < 10 ? "0" : "") + minutes;
            seconds = (seconds < 10 ? "0" : "") + seconds;
            
            var currentDateTime = year + "/" + month + "/" + day + " " + hours + ":" + minutes + ":" + seconds;
            

            var message = $(".checkout_message").val();
            var employee_id = $(".employee_id").val();

            if(!latitude || !longitude){
                alert("Please Check your browser Settings and Allow Location !")
	        }else{
                var result = {}
                result['employee_id'] = employee_id
                result['message'] = message
                result['latitude'] = latitude
                result['longitude'] = longitude
                ajax.jsonRpc('/check/get_sh_attendance_manual', 'call', result).then( function(res){
                });
	        }

            ajax.jsonRpc('/check/get_sh_attendance_worked_time', 'call', result).then( function(res){
                console.log(res);

                
                var checkin_time = $("#worked_time");
                checkin_time.text(""+res+"");
            });

            var checkin_time = $("#checkout_time");
            checkin_time.text(""+currentDateTime+"");

            
            
            $("div.checkin").hide();
            $("div.checkout").hide();
            $("div.after_checkout").show();
            $("div.after_checkin").hide();
        },

        async _onClickAfterChechOutButton() {
            $("div.checkin").show();
            $("div.checkout").hide();
            $("div.after_checkout").hide();
            $("div.after_checkin").hide();
        },
       
    });
});
