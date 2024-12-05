document.getElementById("submit-answer").addEventListener("click", function () {
    // Récupérer la réponse attendue depuis l'attribut data
    const answerBox = document.getElementById("answer-box");
    const expectedAnswer = parseInt(answerBox.getAttribute("data-expected"));

    // Récupérer la réponse de l'utilisateur
    const userAnswer = parseInt(document.getElementById("user-answer").value);

    // Afficher la boîte des réponses
    answerBox.classList.remove("hidden");

    // Vérifier si la réponse de l'utilisateur est correcte
    if (userAnswer === expectedAnswer) {
        document.getElementById("right-answer").classList.remove("hidden");
        document.getElementById("wrong-answer").classList.add("hidden");
    } else {
        document.getElementById("wrong-answer").classList.remove("hidden");
        document.getElementById("right-answer").classList.add("hidden");
    }

    // Cacher le champ d'entrée après soumission
    document.getElementById("user-input-box").classList.add("hidden");
});