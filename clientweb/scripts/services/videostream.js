/**
 * Created by viller_m on 21/09/2015.
 */
'use strict';

angular.module('myApp')
  .factory('VideoStream', function ($q) {
    var stream;
    return {
      get: function () {
        if (stream) {
          return $q.when(stream);
        } else {
          var d = $q.defer();
          navigator.getUserMedia({
            video: true,
            audio: true
          }, function (s) {
            stream = s;
            d.resolve(stream);
          }, function (e) {
            d.reject(e);
          });
          return d.promise;
        }
      }
    };
  });