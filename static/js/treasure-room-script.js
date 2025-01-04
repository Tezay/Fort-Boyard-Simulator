// Variables globales
const gameContainer = document.getElementById('game-container');
const timerDisplay = document.getElementById('timer');
const scoreDisplay = document.getElementById('score');
const gameOverForm = document.getElementById('game-over-form');
const finalScoreInput = document.getElementById('final-score');
let score = 0;
let timeRemaining = 20;
const totalCoins = 30;

// Fonction pour générer des pièces aléatoires
function generateCoins() {
    for (let i = 0; i < totalCoins; i++) {
        const coin = document.createElement('div');
        coin.classList.add('coin');
        coin.style.top = `${Math.random() * 90}%`;
        coin.style.left = `${Math.random() * 90}%`;
        gameContainer.appendChild(coin);

        // Ajouter un événement pour récupérer la pièce
        coin.addEventListener('click', () => {
            score++;
            scoreDisplay.textContent = `Score : ${score}`;
            coin.remove();
        });
    }
}

// Fonction pour gérer le timer
function startTimer() {
    const timerInterval = setInterval(() => {
        timeRemaining--;
        timerDisplay.textContent = `Temps restant : ${timeRemaining}s`;

        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            endGame();
        }
    }, 1000);
}

// Fonction pour terminer le jeu
function endGame() {
    // Soumettre le score final à Flask
    finalScoreInput.value = score;
    gameOverForm.submit();
}

// Lancer le jeu au chargement de la page
window.onload = () => {
    generateCoins();
    startTimer();
};