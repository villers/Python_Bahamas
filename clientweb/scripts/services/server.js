/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .factory('Server', function($websocket, $rootScope) {
        var ws = $websocket($rootScope.address);
        var collection = [];

        ws.onMessage(function(event) {
            console.log('message: ', event);
            var data = JSON.parse(event.data);
            switch(data.Request) {
                case 0: // login
                    console.log('Login Request', data);
                    $rootScope.$broadcast('login', data);
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