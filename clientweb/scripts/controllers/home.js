/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .controller('HomeCtrl', function ($location, $rootScope, $scope, Server) {
        console.log(Server);

        // Réception des événements
        $scope.$on('login', function(events,args){
        	console.log(args);
        	if (args.Status === 200) {
        		 $location.path('/room');
        	} else {
        		$scope.error = args.Message;
        	}
        });

        // Demande de connexion
        $scope.doConnexion = function(){
        	$rootScope.login = $scope.login;
        	$rootScope.address = $scope.address;
        	Server.send({ "request": 0, "Message": $scope.login });
        }
    });