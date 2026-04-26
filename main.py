import praw
import time

# Configuración del bot - NUNCA hardcodees tus credenciales aquí.
# Usa variables de entorno o un archivo .env separado.
reddit = praw.Reddit(
    client_id='TU_CLIENT_ID',
    client_secret='TU_CLIENT_SECRET',
    user_agent='script:BakeryMarketResearch:v1.0 (by /u/TU_USUARIO_REDDIT)'
)


def fetch_recent_discussions(subreddit_name, keywords):
    """
    Busca publicaciones recientes en un subreddit que contengan palabras clave.
    """
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.search(keywords, sort='new', limit=10):
        print(f"Título: {submission.title}")
        print(f"URL: {submission.url}")
        print("-" * 20)


if __name__ == "__main__":
    # Ejemplo de uso: buscar problemas de costos en r/bakery
    TARGET_SUB = "bakery"
    SEARCH_TERMS = "costing OR pricing OR business"

    print(f"Iniciando búsqueda en r/{TARGET_SUB}...")
    fetch_recent_discussions(TARGET_SUB, SEARCH_TERMS)
