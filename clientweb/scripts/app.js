/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';
var angular;
angular
    .module('myApp', [
        'ngRoute',
        'ngWebSocket',
        'ngStorage'
    ])
    .config(function ($routeProvider, $compileProvider) {
        $routeProvider
            .when('/room/:roomName', {
                templateUrl: 'views/room.html',
                controller: 'RoomCtrl'
            })
            .when('/room', {
                templateUrl: 'views/listRoom.html',
                controller: 'ListRoomCtrl'
            })
            .when('/home', {
                templateUrl: 'views/home.html',
                controller: 'HomeCtrl'
            })
            .otherwise({
                redirectTo: '/home'
            });

        $compileProvider.aHrefSanitizationWhitelist(/^\s*(https?|ftp|file|blob):|data:image\//);
    })
    .constant('config', {
        WEBSOCKETURL: 'ws://localhost:3334',
        HASH: 'FDSl4sCSdSF+f4'
    })
    .run(function($rootScope, $location){
        if (!$rootScope.login) {
            $location.path('/home');
        }
    });
