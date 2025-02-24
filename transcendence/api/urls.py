from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views
from .views import (
    AnonymizeAccountView,
    AuthenticateMatchPlayerView,
    AuthenticateTournamentPlayerView,
    ConfirmTournamentParticipationView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenValidateView,
    CustomUser,
    DeleteAccountView,
    FriendsOnlineStatusView,
    ListFriendsView,
    LogoutView,
    PendingTournamentAuthenticationsView,
    PongMatchDetail,
    PongMatchList,
    PongScoreView,
    RankingView,
    RemoveFriendView,
    RespondToFriendRequestView,
    SendFriendRequestView,
    TournamentCreationView,
    TournamentFinalizationView,
    TournamentMatchesView,
    TournamentPlayersView,
    TournamentSearchView,
    UploadAvatarView,
    UserDetailView,
    UserRegisterView,
    UserTournamentsView,
    ViewFriendRequestsView,
	Toggle2FAView,
	Verify2FALoginView,
	Session2FAView,
    check_player_exists,
)

urlpatterns = [
    path("user/tournaments/", UserTournamentsView.as_view(), name="user-tournaments"),
    path("results/", PongMatchList.as_view(), name="pongmatch-list"),
    path("results/<int:pk>/", PongMatchDetail.as_view(), name="pongmatch-detail"),
    path("scores/", PongScoreView.as_view(), name="pong-score"),
    path("scores/<int:pk>/", PongScoreView.as_view(), name="pong-score-detail"),
	# path("api/auth/", include("api.auth.urls")),
    path("auth/login/", CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/refresh/", CustomTokenRefreshView.as_view(), name="token_refresh"),
	path("auth/toggle-2fa/", Toggle2FAView.as_view(), name="toggle-2fa"),
    # path("auth/verify-otp/", VerifyOTPView.as_view(), name="verify-otp"),
	# path("auth/enable-2fa/", Enable2FAView.as_view(), name="enable-2fa"),
    path("auth/verify-2fa-login/", Verify2FALoginView.as_view(), name="verify-2fa-login"),
	path("auth/session-2fa/", Session2FAView.as_view(), name="session-2fa"),
    path("auth/register/", UserRegisterView.as_view(), name="user_register"),
    path("auth/validate/", CustomTokenValidateView.as_view(), name="token_validate"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path(
        "auth/anonymize-account/",
        AnonymizeAccountView.as_view(),
        name="anonymize-account",
    ),
    path("auth/delete-account/", DeleteAccountView.as_view(), name="delete_account"),
    path(
        "auth/match-player/",
        views.AuthenticateMatchPlayerView.as_view(),
        name="authenticate_match_player",
    ),
    path(
        "auth/tournament-player/<int:tournament_id>/",
        AuthenticateTournamentPlayerView.as_view(),
        name="authenticate_tournament_player",
    ),
    path("auth/user/", UserDetailView.as_view(), name="user-detail"),
    path("auth/upload-avatar/", UploadAvatarView.as_view(), name="upload_avatar"),
    path("friends/list/", ListFriendsView.as_view(), name="list_friends"),
    path("friends/remove/", RemoveFriendView.as_view(), name="remove_friend"),
    path("friends/status/", FriendsOnlineStatusView.as_view(), name="friends_status"),
    path(
        "friends/send-request/",
        SendFriendRequestView.as_view(),
        name="send_friend_request",
    ),
    path(
        "friends/requests/",
        ViewFriendRequestsView.as_view(),
        name="view_friend_requests",
    ),  # View pending requests
    path(
        "friends/respond/",
        RespondToFriendRequestView.as_view(),
        name="respond_friend_request",
    ),  # Accept/Decline reques
    path("tournament/new/", TournamentCreationView.as_view(), name="new_tournament"),
    path(
        "tournament/finalize/<int:tournament_id>/",
        TournamentFinalizationView.as_view(),
        name="finalize_tournament",
    ),
    path(
        "tournament/players/<int:tournament_id>/",
        TournamentPlayersView.as_view(),
        name="tournament_players",
    ),
    path(
        "tournament/matches/",
        TournamentMatchesView.as_view(),
        name="tournament_matches",
    ),
    path("user/exists/", views.check_user_exists, name="check_user_exists"),
    path(
        "user/pending-tournament-authentications/",
        PendingTournamentAuthenticationsView.as_view(),
        name="pending-tournament-authentications",
    ),
    path("player/exists/", check_player_exists, name="check_player_exists"),
    path("ranking/", RankingView.as_view(), name="ranking"),
    path("tournaments/", TournamentSearchView.as_view(), name="search_tournaments"),
    path(
        "auth/confirm-participation/<int:tournament_id>/",
        ConfirmTournamentParticipationView.as_view(),
        name="confirm-tournament-participation",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# This ensures that media folder (which can also be mounted as a volume in production setups) is properly linked to Django project.
