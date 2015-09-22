/**
 * Created by viller_m on 22/09/2015.
 */
'use strict';

angular.module('myApp')
    .controller('ListRoomCtrl', function (Server, $scope, $rootScope) {
        // Demande la liste des rooms
        $scope.refreshList = function() {
            Server.send({ "request": 1, "Message": ""});
        };

        // Récupération de la liste des rooms
        $scope.$on('listRooms', function(events,args){
            $scope.listRooms = args.Message;
        });

        // Demande de création de la room
        $scope.createRoom = function() {
            Server.send({ "request": 2, "Message": $scope.roomName });
        };

        // Création d'une nouvelle room
        $scope.$on('createRoom', function(events,args){
            $scope.refreshList();
            $scope.roomName = "";
            $scope.create = false;
        });

        $scope.refreshList();
    });