document.addEventListener('DOMContentLoaded', function () {

    document.querySelector('form').onsubmit = function () {
        if (page === "comentarios") {
            alert("Comentario submetido.");
            localStorage.setItem('refresh',"1");
        }

        if (page === "quizz") {
            alert("Quizz submetido.");
        }

        if (page === "contacto") {
            alert("Contacto submetido. Espere contacto nas próximas 24.");
        }
    }
})