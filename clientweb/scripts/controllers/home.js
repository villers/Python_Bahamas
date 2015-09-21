/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .controller('HomeCtrl', function ($location, $scope, Server) {
        console.log(Server);
        Server.send({ "request": 0, "Message": "nickName" });
    });