/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
  .controller('RoomCtrl', function (Server, $scope, $rootScope) {
    Server.send({ "request": 1, "Message": ""});

    // Récupération de la liste des rooms
    $scope.$on('listRooms', function(events,args){
      $scope.listRooms = args.Message;
    });

    // Création d'une nouvelle room
    $scope.$on('createRoom', function(events,args){
      console.log("createroom", args)
      //$scope.createRoom = args.Message;
    });
   
    $scope.toggleSelect = function(){
      $scope.selectRoom = (!$scope.selectRoom)? true : false;
    }

    $scope.toggleCreate = function(){
      $scope.createRoom = (!$scope.createRoom)? true : false;
    }

  });