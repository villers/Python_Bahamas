/**
 * Created by viller_m and sioly_t on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .controller('RoomCtrl', function ($location, Server, $scope, $routeParams, VideoStream, $sce) {
        $scope.peers = [];

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

        // Rejoins la room
        $scope.$on('joinRoom', function(events,args){
            $scope.doListUsers();
        });

        // Demande la liste des rooms
        $scope.refreshList = function() {
            Server.send({ "request": 1, "Message": ""});
        };

        // Demande de création d'une nouvelle room
        $scope.doCreateRoom = function(){
            Server.send({ "request": 2, "Message": $scope.createRoomName });
        };

        // Demande à rejoindre une room
        $scope.doJoinRoom = function(){
            $scope.selectRoomName = $routeParams.roomName;
            Server.send({ "request": 5, "Message": $routeParams.roomName });
        };

        // Demande de récupération de la liste des users
        $scope.doListUsers = function(){
            Server.send({ "request": 3, "Message": $routeParams.roomName });
        };

        $scope.toggleSelect = function(){
            $scope.selectRoom = (!$scope.selectRoom);
        };

        $scope.toggleCreate = function(){
            $scope.createRoom = (!$scope.createRoom);
        };

        $scope.changeRoom = function() {
            $location.path('room/'+$scope.selectRoomName);
        };

        $scope.test = function(event) {
            console.log($(event.target).css('width','100px'));
        };

        $scope.closeCamera = function(event) {
            console.log($(event.target).css('display','none'));
        };

        $scope.refreshList();
        $scope.doJoinRoom();


        if (!window.RTCPeerConnection || !navigator.getUserMedia) {
            alert('WebRTC is not supported by your browser. You can try the app with Chrome and Firefox.');
            return false;
        }

        var webrtc = new SimpleWebRTC({
            localVideoEl: 'localVideo',
            remoteVideosEl: '',
            autoRequestMedia: true,
            debug: false,
            detectSpeakingEvents: true,
            autoAdjustMic: false
        });

        webrtc.on('readyToCall', function () {
            if ($scope.selectRoomName) {
                webrtc.joinRoom($scope.selectRoomName);
            }
        });

        // a peer video has been added
        webrtc.on('videoAdded', function (video, peer) {
            console.log('video added', peer);
            console.log(video);
            video = $(video);

            var item = {
                src: video.attr('src'),
                id: video.attr('id')
            };
            $scope.peers.push(item);
            $scope.$apply();
        });
    });