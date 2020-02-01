

	Ver graficamente as músicas que escutei desde que tenho o Spotify, agrupadas por Gênero, Artista e Ano de Lançamento.
	Ver qual gênero eu mais ouço, agrupado por mês (e estação do ano, consequentemente - levar em conta mudança de hemisfério)
	Ver quais músicas eu ouço muito e não estão na minha playlist
	
	Artista:
		Fácil, basta ler o json, agrupar por artista e somar os milisegundos
	
	Gênero e Ano de Lançamento:
		Usar API lastfm.com que me retorna o gênero do artista e fazer a chamada por nome do artista
			http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist=Royal%20Blood&api_key=068ed6fd95768b4a6a8f671fc35dccd4&format=json
			
			
			

	1) Criar estrutura de pasta e abrir projeto no VSCode
	2) Criar pastas Data e Config
	3) Colocar UserAgent, API key, URL e endpoint 
	

	1) Funções format_query, load_config, load_data
	2) Funções get_artistInfo
	
	