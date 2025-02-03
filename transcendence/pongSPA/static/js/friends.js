
export function addFriend(friendUsername) {
	fetch("/api/friends/add/", {
	  method: "POST",
	  headers: {
		"Content-Type": "application/json",
	  },
	  credentials: "include",
	  body: JSON.stringify({ username: friendUsername }),
	})
	  .then((response) => response.json())
	  .then((data) => {
		if (data.error) {
		  alert("Erreur : " + data.error);
		} else {
		  alert(data.message);
		  fetchFriends(); // Refresh the friend list
		}
	  })
	  .catch((error) => {
		console.error("Erreur lors de l'ajout d'ami :", error);
		alert("Une erreur est survenue.");
	  });
  }

export function removeFriend(friendUsername) {
	if (!confirm(`Voulez-vous vraiment supprimer ${friendUsername} de votre liste d'amis ?`)) {
	  return;
	}
  
	fetch("/api/friends/remove/", {
	  method: "DELETE",
	  headers: {
		"Content-Type": "application/json",
	  },
	  credentials: "include",
	  body: JSON.stringify({ username: friendUsername }),
	})
	  .then((response) => response.json())
	  .then((data) => {
		if (data.error) {
		  alert("Erreur : " + data.error);
		} else {
		  alert(data.message);
		  fetchFriends(); // Refresh friend list
		}
	  })
	  .catch((error) => {
		console.error("Erreur lors de la suppression d'ami :", error);
		alert("Une erreur est survenue.");
	  });
  }


export function fetchFriends() {
	fetch("/api/friends/list/", {
	  method: "GET",
	  credentials: "include",
	})
	  .then((response) => response.json())
	  .then((friendsData) => {
		// Now fetch friend statuses
		fetch("/api/friends/status/", {
		  method: "GET",
		  credentials: "include",
		})
		  .then((statusResponse) => statusResponse.json())
		  .then((statusData) => {
			const friendList = document.getElementById("friendList");
			friendList.innerHTML = "";
  
			friendsData.friends.forEach((friend) => {
			  // Find corresponding status in statusData
			  const friendStatus = statusData.friends_status.find(
				(status) => status.username === friend.username
			  );
  
			  const isOnline = friendStatus ? friendStatus.is_online : false;
			  const lastSeen = friendStatus ? friendStatus.last_seen : "Never";
  
			  const statusBadge = isOnline
				? `<span class="badge bg-success">🟢 En ligne</span>`
				: `<span class="badge bg-secondary">⚫ Hors ligne (vu: ${lastSeen})</span>`;

		  const listItem = document.createElement("li");
		  listItem.className = "list-group-item d-flex justify-content-between align-items-center";
		  listItem.innerHTML = `
			<span>${friend.username} ${statusBadge}</span>
			<button class="btn btn-danger btn-sm remove-friend" data-username="${friend.username}">❌ Supprimer</button>
		  `;
		  friendList.appendChild(listItem);
		});
		// event listeners to remove buttons
		document.querySelectorAll(".remove-friend").forEach((button) => {
			button.addEventListener("click", (event) => {
			  const friendUsername = event.target.getAttribute("data-username");
			  removeFriend(friendUsername);
			});
		});
	  })
	  .catch((error) => console.error("Erreur lors de la récupération des statuts d'amis :", error));
    })
	.catch((error) => console.error("Erreur lors de la récupération des amis :", error));
  }