/**
 * Created by viller_m and sioly_t on 21/09/2015.
 */
'use strict';

angular.module('myApp')
  .controller('RoomCtrl', function ($location, Server, $scope, $rootScope) {
    Server.send({ "request": 0, "Message": ""});
    Server.send({ "request": 1, "Message": ""});

    // Récupération de la liste des rooms
    $scope.$on('listRooms', function(events,args){
      $scope.listRooms = args.Message;
    });

    // Récupération de la liste des users
    $scope.$on('listUsers', function(events,args){
      $scope.listUsers = args.Message;
    });

    // Création d'une nouvelle room
    $scope.$on('createRoom', function(events,args){
      if (args.Status === 200) {
        $location.path('room/'+$scope.createRoomName);
      }
    });
   
    $scope.toggleSelect = function(){
      $scope.selectRoom = (!$scope.selectRoom)? true : false;
    }

    $scope.toggleCreate = function(){
      $scope.createRoom = (!$scope.createRoom)? true : false;
    }

    // Demande de création d'une nouvelle room
      $scope.doCreateRoom = function(){
        Server.send({ "request": 2, "Message": $scope.createRoomName });
      }

      // Demande de création d'une nouvelle room
      $scope.doSelectRoom = function(){
        Server.send({ "request": 2, "Message": $scope.createRoomName });
      }

    // Demande de récupération de la liste des users
      $scope.doListUsers = function(){
        Server.send({ "request": 3, "Message": $scope.createRoomName });
      }

  });