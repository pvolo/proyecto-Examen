$(document).ready(function () {
    $.getJSON('https://digidates.de/api/v1/unixtime', function (data) {
        console.log("Datos recibidos:", data);
        var tiempoLocal = new Date(data.time * 1000); 
        var tiempoLocalString = tiempoLocal.toLocaleString(); 
        $("#cuadro3").text("Tiempo actual en hora local: " + tiempoLocalString);
    }).fail(function () {
        console.log("Error al cargar los datos del tiempo.");
        $("#cuadro3").text("Error al cargar los datos del tiempo.");
    });
});

