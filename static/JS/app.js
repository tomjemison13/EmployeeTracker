(function () {
	var app = angular.module('BSU', []);
	
	app.controller('BSUController',['$http',function ($http) {
		var BSU = this;
		BSU.employees = [];
		
		$http.get('http://mydomain.com:8888/api/v1/employees').success(function(data){
			BSU.employees = data.employees;
		});
		
}]);
	
})();