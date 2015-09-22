/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
    .directive('videoPlayer', function ($sce) {
        return {
            template: '<div><video ng-src="{{trustSrc()}}" autoplay></video></div>',
            restrict: 'E',
            replace: true,
            scope: {
                vidSrc: '@'
            },
            link: function (scope) {
                console.log('Initializing video-player');
                scope.trustSrc = function () {
                    if (!scope.vidSrc) {
                        return undefined;
                    }
                    return $sce.trustAsResourceUrl(scope.vidSrc);
                };
            }
        };
    });