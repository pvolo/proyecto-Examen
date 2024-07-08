
fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const temperatura = data.main.temp;
        const descripcion = data.weather[0].description;

        const weatherData = document.getElementById('weatherData');
        weatherData.innerHTML = `<p>Temperatura: ${ temperatura}°C</p>
                                 <p >Descripción: ${descripcion}</p>`;
    })
    .catch(error => {
        console.log('Error al obtener los datos del Clima:', error);
        const weatherData = document.getElementById('weatherData');
        weatherData.innerHTML = '<p> Ocurrió un error </p>';
    });
