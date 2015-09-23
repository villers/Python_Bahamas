/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular
  .module('myApp', [
    'ngRoute',
    'ngWebSocket',
    'ngStorage'
  ])
  .config(function ($routeProvider) {
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
  })
  .constant('config', {
      WEBSOCKETURL: 'ws://10.12.181.128:3334'
  })
  .run(function($rootScope, $location){
      if (!$rootScope.login) {
        $location.path('/home');
      }
  });
