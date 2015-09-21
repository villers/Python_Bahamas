/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular
  .module('myApp', [
    'ngRoute',
    'ngWebSocket'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/room/:roomId', {
        templateUrl: 'views/room.html',
        controller: 'RoomCtrl'
      })
      .when('/room', {
        templateUrl: 'views/room.html',
        controller: 'RoomCtrl'
      })
      .when('/home', {
        templateUrl: 'views/home.html',
        controller: 'HomeCtrl'
      })
      .otherwise({
        redirectTo: '/home'
      });
  })
  .run(function($rootScope){
    $rootScope.address = "ws://localhost:3334";
  });