export function createTournamentForm() {
    const appDiv = document.getElementById("app");
    appDiv.innerHTML = `
      <h2>Créer un tournoi</h2>
      <form id="tournamentForm">
        <input type="text" id="tournamentName" placeholder="Nom du tournoi" required>
        <div id="playerContainer"></div>
        <button type="button" id="addPlayerButton">Ajouter un joueur</button>
        <button type="button" id="submitButton">Soumettre</button>
      </form>
    `;
    
    const playerContainer = document.getElementById('playerContainer');
    const addButton = document.getElementById('addPlayerButton');
    const submitButton = document.getElementById('submitButton');
    let playerCount = 1;
    let players = [];
    
    addButton.onclick = () => {
        const playerDiv = document.createElement('div');
        playerDiv.innerHTML = `Joueur n° : ${playerCount} <input type="text" placeholder="Pseudo">`; playerContainer.appendChild(playerDiv);
        playerCount++;
    };

    submitButton.onclick = () => {
        const tournamentName = document.getElementById('tournamentName').value;
        players = Array.from(playerContainer.children).map(div => div.querySelector('input').value);
        sendPlayersToAPI(tournamentName, players);
    };

    function sendPlayersToAPI(tournamentName, players) {
        fetch("/api/tournament/new/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        body: JSON.stringify({ tournament_name: tournamentName, players }),
        })
        .then(response => response.json())
        .then(data => console.log('Success:', data))
        .catch((error) => console.error('Error:', error));
    }
}

