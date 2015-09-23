/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .factory('Server', function($websocket, $rootScope, config) {
        var ws = $websocket(config.WEBSOCKETURL);
        var collection = [];

        ws.onMessage(function(event) {
            console.log('message: ', event);
            var data = JSON.parse(event.data);
            switch(data.Request) {
                case 0: // login
                    $rootScope.$broadcast('login', data);
                    break;
                case 1: // listrooms
                    $rootScope.$broadcast('listRooms', data);
                    break;
                case 2: // create a room
                    $rootScope.$broadcast('createRoom', data);
                    break;
                case 3: // list users from a room
                    $rootScope.$broadcast('listUsers', data);
                    break;
                case 4: // leave a room
                    $rootScope.$broadcast('leaveRoom', data);
                    break;
                case 5: // Join a room
                    $rootScope.$broadcast('joinRoom', data);
                    break;
                default:
                    console.log('Bad Request', data);
                    break;
            }
            collection.push(JSON.parse(event.data));
        });

        ws.onError(function(event) {
            console.log('connection Error', event);
        });

        ws.onClose(function(event) {
            console.log('connection closed', event);
        });

        ws.onOpen(function() {
            console.log('connection open');
        });

        return {
            collection: collection,
            status: function() {
                return ws.readyState;
            },
            send: function(message) {
                if (angular.isString(message)) {
                    ws.send(message);
                }
                else if (angular.isObject(message)) {
                    ws.send(JSON.stringify(message));
                }
            }

        };
});