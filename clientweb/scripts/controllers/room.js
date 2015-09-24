/**
 * Created by viller_m and sioly_t on 21/09/2015.
 */
'use strict';

angular.module('myApp')

    .controller('RoomCtrl', function ($location, Server, $scope, $routeParams, VideoStream, $sce, $rootScope) {
        $scope.peers = [];
        $scope.messages = [];
        $scope.listUsers = [];

        // Récupération de la liste des rooms
        $scope.$on('listRooms', function(events,args){
            $scope.listRooms = args.Message;
        });

        // Récupération de la liste des users
        $scope.$on('listUsers', function(events,args){
            $scope.listUsers = args.Message;
            console.log(args.Message);
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

        $scope.quitRoom = function quitRoom() {
            webrtc.stopLocalVideo();
            webrtc.leaveRoom();
            webrtc.disconnect();
            Server.send({ "request": 4, "Message": $routeParams.roomName });
        };

        $scope.changeRoom = function() {
            $scope.quitRoom();
            $location.path('room/'+$scope.selectRoomName);
        };

        $scope.ctrlCamera = function(event) {

            if($(event.target).hasClass("visibleTrue")){
                $(event.target).removeClass('visibleTrue');
                $(event.target).addClass('visibleFalse');
                $('.visibleTrue').hide();
            }else if($(event.target).hasClass("visibleFalse")){
                $(event.target).removeClass('visibleFalse');
                $(event.target).addClass('visibleTrue');
                $('.visibleTrue').show();
            }
        };


        $scope.sendMessage = function() {
            if($scope.message != ""){
                webrtc.sendToAll('chat', {
                    message: $scope.message,
                    nick: webrtc.config.nick
                });
                $scope.message = '';
            }
        };

        $scope.refreshList();
        $scope.doJoinRoom();

        var webrtc = new SimpleWebRTC({
            localVideoEl: 'localVideo',
            remoteVideosEl: '',
            autoRequestMedia: true,
            debug: false,
            detectSpeakingEvents: true,
            autoAdjustMic: false,
            nick: $rootScope.login,
            socketio: {'force new connection':true}
        });

        webrtc.on('readyToCall', function () {
            if ($scope.selectRoomName) {
                webrtc.joinRoom($scope.selectRoomName);
            }
        });

        webrtc.on('videoAdded', function (video, peer) {
            console.log('video added', peer);
            video = $(video);
            var item = {
                src: $sce.trustAsResourceUrl(video.attr('src')),
                id: video.attr('id'),
                nick: peer.nick
            };

            if (peer.nick != $scope.listUsers.Clients[{'login', x}]) {
                $scope.listUsers.Clients.push({
                    "Ip": video.attr('id'),
                    "Login": peer.nick
                });
            }

            $scope.peers.push(item);
            if(!$scope.$$phase) {
                $scope.$apply();
            }
        });

        webrtc.on('videoRemoved', function (video, peer) {
            console.log('video removed ', video, peer);
            $scope.peers = $scope.peers.filter(function(item) {
                console.log(item.nick, peer.nick);
                return item.nick != peer.nick;
            });
            if(!$scope.$$phase) {
                $scope.$apply();
            }
        });

        webrtc.connection.on('message', showMessage);
        webrtc.on('message', showMessage);

        function showMessage(data) {
            if(data.type === 'chat'){
                console.log(data.payload.nick + ':' + data.payload.message);
                $scope.messages.push(data.payload.nick + ': ' + data.payload.message);
                if(!$scope.$$phase) {
                    $scope.$apply();
                }
                $('.container_chat').animate({'scrollTop': $('.container_chat')[0].scrollHeight}, 'fast');
            }
        }
    });