(function(){
	var app = angular.module("app", []);

	var mainCtrl = function($scope,$http,$interval){
    $scope.countdown = 5;

    var decrementCountdown = function(){
      	$scope.countdown -=1;

        if($scope.countdown <1){
        	alert("End count down");
        }
      };

      var startCountdown = function(){
				$interval(decrementCountdown, 1000, $scope.countdown);
      }
      startCountdown();

  };

  app.controller("mainCtrl", mainCtrl);
}());