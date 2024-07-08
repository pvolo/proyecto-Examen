const formulasioregistro = document.getElementById            
const formularioregistro = document.getElementById('formularioregistro');
const usuario = document.getElementById('usuario');
const correo = document.getElementById('correo')
const constraseña = document.getElementById('constraseña');

const expresiones = {
    usuario: /^[a-zA-Z0-9_-]{3,16}$/,
    correo: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
    contraseña: /^(.){4,12}$/ 
}
const mensajes = {
    usuario: 'Por favor ingresa un usuario válido.',
    correo: 'Por favor, ingrese un correo válido',
    contraseña: 'Por favor ingresa una contraseña válida.'
}

usuario.addEventListener('input', () => validarCampo(expresiones.usuario, usuario, mensajes.usuario));
correo.addEventListener('input', () => validarCampo(expresiones.correo, correo, mensajes.correo));
contraseña.addEventListener('input', () => validarCampo(expresiones.contraseña, contraseña, mensajes.contraseña));

function validarCampo(expresion, input, mensaje) {
    if (expresion.test(input.value)) {
        input.classList.remove('is-invalid');
        input.classList.add('is-valid');
        const error = input.nextElementSibling;
        if (error && error.classList.contains('invalid-feedback')) {
            error.remove();
        }
    } else {
        input.classList.add('is-invalid');
        input.classList.remove('is-valid');
        const error = input.nextElementSibling;
        if (!error || !error.classList.contains('invalid-feedback')) {
            const divError = document.createElement('div');
            divError.classList.add('invalid-feedback');
            input.parentNode.appendChild(divError);
        }
        input.nextElementSibling.innerText = mensaje;
    }
}
formularioregistro.addEventListener('submit', function(event) {
    event.preventDefault(); 

    validarCampo(expresiones.usuario, usuario, mensajes.usuario);
    validarCampo(expresiones.correo, correo, mensajes.correo);
    validarCampo(expresiones.contraseña, contraseña, mensajes.contraseña);

    if (usuario.classList.contains('is-valid') && correo.classList.contains('is-valid') && contraseña.classList.contains('is-valid')) {
        this.submit();
    }
});