// Funzione per verificare il login
function verificaLogin() {
    // Prendiamo gli elementi di input dal form
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Controlliamo che i campi non siano vuoti
    if (username && password) {
        // Simula il login (puoi aggiungere una verifica più complessa qui)
        alert("Login effettuato con successo!");
        
        // Reindirizza alla pagina principale (home)
        window.location.href = "home.html"; // Sostituisci con il nome del file della tua homepage
    } else {
        // Mostra un messaggio di errore se i campi sono vuoti
        alert("Per favore, inserisci username e password.");
    }
}

// Funzione per andare alla seconda pagina
function vaiAallaPagina2() {
    // Reindirizza alla pagina 2
    window.location.href = "pagina2.html";
}

// Funzione per tornare alla home   
function ritornaAllaHome() {
    window.location.href = "home.html";
}
