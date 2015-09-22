/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .factory('Server', function($websocket, $rootScope, config) {
        var ws = $websocket(config.SIGNALIG_SERVER_URL);
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

                case 3: // list of users
                    $rootScope.$broadcast('listUsers', data);
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