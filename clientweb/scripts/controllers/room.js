/**
 * Created by viller_m and sioly_t on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .controller('RoomCtrl', function ($location, Server, $scope, $routeParams, VideoStream, $sce, $rootScope, config) {
        // gestion du scope
        $scope.peers = [];
        $scope.messages = [];
        $scope.listUsers = [];
        $scope.mute = false;

        // Rejoins la room
        $scope.$on('joinRoom', function(events, args){
            console.log('connected')
        });

        // Demande à rejoindre une room
        $scope.doJoinRoom = function(){
            $scope.selectRoomName = $routeParams.roomName;
            Server.send({ "request": 5, "Message": $routeParams.roomName });
        };

        $scope.quitRoom = function quitRoom() {
            webrtc.stopLocalVideo();
            webrtc.leaveRoom();
            webrtc.disconnect();
            Server.send({ "request": 4, "Message": $routeParams.roomName });
        };

        $scope.ctrlCamera = function(event) {
            if ($(event.target).hasClass("visibleTrue")) {
                $(event.target).removeClass('visibleTrue');
                $(event.target).addClass('visibleFalse');
                $('.visibleTrue').hide();
            } else if($(event.target).hasClass("visibleFalse")) {
                $(event.target).removeClass('visibleFalse');
                $(event.target).addClass('visibleTrue');
                $('.visibleTrue').show();
            }
        };

        $scope.sendMessage = function() {
            if ($scope.message != "") {
                webrtc.sendToAll('chat', {
                    message: $scope.message,
                    nick: webrtc.config.nick
                });
                showMessage({
                    type: 'chat',
                    payload: {
                        nick: $rootScope.login,
                        message: $scope.message
                    }
                });
                $scope.message = '';
            }
        };

        $scope.doJoinRoom();

        // gestion du webrtc
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
                webrtc.joinRoom(config.HASH + $scope.selectRoomName + config.HASH);
            }
        });

        webrtc.on('videoAdded', function (video, peer) {
            console.log('video added', peer);
            video = $(video);
            $scope.listUsers.push(peer.nick);
            $scope.peers.push({
                src: $sce.trustAsResourceUrl(video.attr('src')),
                id: video.attr('id'),
                nick: peer.nick
            });
            if (!$scope.$$phase) {
                $scope.$apply();
            }
        });

        webrtc.on('videoRemoved', function (video, peer) {
            console.log('video removed ', video, peer);
            $scope.listUsers = $scope.listUsers.filter(function(item) {
                return item != peer.nick;
            });
            $scope.peers = $scope.peers.filter(function(item) {
                return item.nick != peer.nick;
            });
            if (!$scope.$$phase) {
                $scope.$apply();
            }
        });

        webrtc.connection.on('message', showMessage);

        // helper
        function showMessage(data) {
            if(data.type === 'chat'){
                $scope.messages.push(data.payload.nick + ': ' + data.payload.message);
                if (!$scope.$$phase) {
                    $scope.$apply();
                }

                if (!$scope.mute) {
                    webrtc.mute('video');
                    webrtc.mute('audio');
                    $('body').prop('muted',true);
                    var audio = new Audio('song/bip.mp3');
                    audio.play();
                }

                var element = $('.container_chat');
                element.animate({'scrollTop': element[0].scrollHeight}, 'fast');
            }
        }

    });