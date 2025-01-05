from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

questions_capitali = [
    {"question": "Qual è la capitale d'Italia?", "options": ["Milano", "Roma", "Napoli", "Torino"], "answer": "Roma"},
    {"question": "Qual è la capitale della Francia?", "options": ["Marsiglia", "Lione", "Parigi", "Nizza"], "answer": "Parigi"},
    {"question": "Qual è la capitale della Germania?", "options": ["Monaco", "Berlino", "Amburgo", "Francoforte"], "answer": "Berlino"},
    {"question": "Qual è la capitale della Spagna?", "options": ["Barcellona", "Madrid", "Valencia", "Siviglia"], "answer": "Madrid"},
    {"question": "Qual è la capitale del Portogallo?", "options": ["Porto", "Lisbona", "Coimbra", "Faro"], "answer": "Lisbona"},
    {"question": "Qual è la capitale del Regno Unito?", "options": ["Liverpool", "Londra", "Manchester", "Edimburgo"], "answer": "Londra"},
    {"question": "Qual è la capitale della Russia?", "options": ["San Pietroburgo", "Mosca", "Kazan", "Novosibirsk"], "answer": "Mosca"},
    {"question": "Qual è la capitale della Cina?", "options": ["Shanghai", "Pechino", "Hong Kong", "Shenzhen"], "answer": "Pechino"},
    {"question": "Qual è la capitale del Giappone?", "options": ["Osaka", "Kyoto", "Tokyo", "Hiroshima"], "answer": "Tokyo"},
    {"question": "Qual è la capitale dell'Australia?", "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"], "answer": "Canberra"},
    {"question": "Qual è la capitale del Canada?", "options": ["Toronto", "Vancouver", "Montreal", "Ottawa"], "answer": "Ottawa"},
    {"question": "Qual è la capitale degli Stati Uniti?", "options": ["New York", "Washington D.C.", "Los Angeles", "Chicago"], "answer": "Washington D.C."},
    {"question": "Qual è la capitale dell'India?", "options": ["Mumbai", "Nuova Delhi", "Chennai", "Bangalore"], "answer": "Nuova Delhi"},
    {"question": "Qual è la capitale del Brasile?", "options": ["San Paolo", "Brasilia", "Rio de Janeiro", "Salvador"], "answer": "Brasilia"},
    {"question": "Qual è la capitale dell'Argentina?", "options": ["Cordoba", "Buenos Aires", "Rosario", "Mendoza"], "answer": "Buenos Aires"},
    {"question": "Qual è la capitale della Turchia?", "options": ["Istanbul", "Ankara", "Izmir", "Bursa"], "answer": "Ankara"},
    {"question": "Qual è la capitale dell'Egitto?", "options": ["Alessandria", "Il Cairo", "Luxor", "Giza"], "answer": "Il Cairo"},
    {"question": "Qual è la capitale della Grecia?", "options": ["Salonicco", "Atene", "Patrasso", "Heraklion"], "answer": "Atene"},
    {"question": "Qual è la capitale della Svezia?", "options": ["Malmo", "Göteborg", "Stoccolma", "Uppsala"], "answer": "Stoccolma"},
    {"question": "Qual è la capitale della Norvegia?", "options": ["Bergen", "Oslo", "Stavanger", "Trondheim"], "answer": "Oslo"},
    {"question": "Qual è la capitale del Messico?", "options": ["Cancún", "Città del Messico", "Guadalajara", "Monterrey"], "answer": "Città del Messico"},
    {"question": "Qual è la capitale della Corea del Sud?", "options": ["Busan", "Seul", "Incheon", "Daegu"], "answer": "Seul"},
    {"question": "Qual è la capitale della Svizzera?", "options": ["Zurigo", "Ginevra", "Berna", "Losanna"], "answer": "Berna"},
    {"question": "Qual è la capitale dei Paesi Bassi?", "options": ["Rotterdam", "Amsterdam", "L'Aia", "Utrecht"], "answer": "Amsterdam"},
    {"question": "Qual è la capitale dell'Austria?", "options": ["Salisburgo", "Vienna", "Graz", "Linz"], "answer": "Vienna"},
    {"question": "Qual è la capitale della Polonia?", "options": ["Cracovia", "Varsavia", "Danzica", "Poznań"], "answer": "Varsavia"},
    {"question": "Qual è la capitale del Sudafrica?", "options": ["Johannesburg", "Pretoria", "Durban", "Città del Capo"], "answer": "Pretoria"},
    {"question": "Qual è la capitale della Nuova Zelanda?", "options": ["Auckland", "Wellington", "Christchurch", "Hamilton"], "answer": "Wellington"},
    {"question": "Qual è la capitale della Corea del Nord?", "options": ["Pyongyang", "Seul", "Busan", "Incheon"], "answer": "Pyongyang"},
    {"question": "Qual è la capitale del Vietnam?", "options": ["Ho Chi Minh", "Hanoi", "Da Nang", "Hue"], "answer": "Hanoi"},
    {"question": "Qual è la capitale della Finlandia?", "options": ["Tampere", "Turku", "Helsinki", "Oulu"], "answer": "Helsinki"},
    {"question": "Qual è la capitale della Tailandia?", "options": ["Chiang Mai", "Bangkok", "Phuket", "Pattaya"], "answer": "Bangkok"},
    {"question": "Qual è la capitale dell'Irlanda?", "options": ["Cork", "Dublino", "Galway", "Limerick"], "answer": "Dublino"},
    {"question": "Qual è la capitale della Norvegia?", "options": ["Oslo", "Bergen", "Stavanger", "Tromsø"], "answer": "Oslo"}
]


questions_sport = [
    {"question": "In quale sport si usa una racchetta per colpire una pallina sopra una rete?", "options": ["Calcio", "Tennis", "Pallavolo", "Rugby"], "answer": "Tennis"},
    {"question": "Qual è il numero massimo di giocatori in una squadra di calcio in campo?", "options": ["9", "10", "11", "12"], "answer": "11"},
    {"question": "In quale sport si cerca di segnare punti lanciando una palla in un canestro?", "options": ["Pallacanestro", "Pallamano", "Tennis", "Pallanuoto"], "answer": "Pallacanestro"},
    {"question": "Qual è il nome del torneo di tennis che si gioca sull'erba a Londra?", "options": ["Roland Garros", "US Open", "Wimbledon", "Australian Open"], "answer": "Wimbledon"},
    {"question": "In quale sport si usa una mazza per colpire una palla lanciata da un avversario?", "options": ["Cricket", "Baseball", "Golf", "Hockey su ghiaccio"], "answer": "Baseball"},
    {"question": "Quale squadra ha vinto il maggior numero di titoli della Champions League?", "options": ["Barcellona", "Bayern Monaco", "Real Madrid", "Manchester United"], "answer": "Real Madrid"},
    {"question": "In quale sport si pratica il 'servizio' come azione iniziale?", "options": ["Tennis", "Pallavolo", "Badminton", "Tutte le precedenti"], "answer": "Tutte le precedenti"},
    {"question": "Qual è il nome dello stadio principale del Barcellona FC?", "options": ["Santiago Bernabéu", "Camp Nou", "Old Trafford", "San Siro"], "answer": "Camp Nou"},
    {"question": "In quale sport si usa una palla ovale?", "options": ["Rugby", "Baseball", "Pallanuoto", "Hockey su prato"], "answer": "Rugby"},
    {"question": "Qual è la durata standard di una partita di calcio?", "options": ["80 minuti", "90 minuti", "70 minuti", "100 minuti"], "answer": "90 minuti"},
    {"question": "In quale sport si gioca con una tavola su onde marine?", "options": ["Surf", "Windsurf", "Kayak", "Vela"], "answer": "Surf"},
    {"question": "Chi è noto come 'il re del calcio'?", "options": ["Diego Maradona", "Lionel Messi", "Pelé", "Cristiano Ronaldo"], "answer": "Pelé"},
    {"question": "In quale sport si utilizza un bastone per spingere un disco?", "options": ["Hockey su prato", "Hockey su ghiaccio", "Cricket", "Baseball"], "answer": "Hockey su ghiaccio"},
    {"question": "Qual è la distanza di una maratona?", "options": ["35 km", "42,195 km", "50 km", "40 km"], "answer": "42,195 km"},
    {"question": "Qual è il colore della maglia del vincitore del Tour de France?", "options": ["Rosso", "Verde", "Giallo", "Blu"], "answer": "Giallo"},
    {"question": "In quale sport si pratica il 'doppio misto'?", "options": ["Badminton", "Tennis", "Tennis da tavolo", "Tutti i precedenti"], "answer": "Tutti i precedenti"},
    {"question": "Quale nazione ha ospitato le Olimpiadi del 2020 (disputate nel 2021)?", "options": ["Cina", "Brasile", "Giappone", "Italia"], "answer": "Giappone"},
    {"question": "In quale sport si gareggia nei 100 metri piani?", "options": ["Nuoto", "Atletica leggera", "Ciclismo", "Sci di fondo"], "answer": "Atletica leggera"},
    {"question": "Qual è lo sport praticato da Michael Phelps?", "options": ["Atletica", "Nuoto", "Ciclismo", "Tennis"], "answer": "Nuoto"},
    {"question": "In quale sport si usa il termine 'ace'?", "options": ["Pallavolo", "Tennis", "Golf", "Baseball"], "answer": "Tennis"},
    {"question": "In quale sport si usa una rete e una palla più piccola rispetto al calcio?", "options": ["Pallavolo", "Tennis", "Badminton", "Pallamano"], "answer": "Pallavolo"},
    {"question": "Chi è considerato il miglior giocatore di basket della NBA di tutti i tempi?", "options": ["Michael Jordan", "LeBron James", "Kobe Bryant", "Shaquille O'Neal"], "answer": "Michael Jordan"},
    {"question": "Quale paese ha ospitato i Mondiali di calcio 2006?", "options": ["Francia", "Germania", "Italia", "Brasile"], "answer": "Germania"},
    {"question": "Qual è lo sport nazionale del Giappone?", "options": ["Judo", "Sumo", "Karate", "Baseball"], "answer": "Sumo"},
    {"question": "Quante medaglie d'oro ha vinto Usain Bolt nella sua carriera olimpica?", "options": ["6", "8", "10", "7"], "answer": "8"},
    {"question": "Quale sport usa un campo chiamato 'diamante'?", "options": ["Cricket", "Baseball", "Pallacanestro", "Pallavolo"], "answer": "Baseball"},
    {"question": "Chi ha vinto il primo titolo di Formula 1?", "options": ["Lewis Hamilton", "Juan Manuel Fangio", "Nino Farina", "Michael Schumacher"], "answer": "Nino Farina"},
    {"question": "In quale sport è famoso Pelé?", "options": ["Basket", "Cricket", "Calcio", "Tennis"], "answer": "Calcio"},
    {"question": "Quale squadra di calcio italiana è nota come 'La Vecchia Signora'?", "options": ["Inter", "Milan", "Juventus", "Roma"], "answer": "Juventus"},
    {"question": "Quale sport si pratica sul ghiaccio con pattini?", "options": ["Hockey su ghiaccio", "Curling", "Pattinaggio di velocità", "Bobsleigh"], "answer": "Hockey su ghiaccio"}
]


questions_storia = [
    {"question": "In quale anno Cristoforo Colombo ha scoperto l'America?", "options": ["1492", "1500", "1453", "1498"], "answer": "1492"},
    {"question": "Chi è stato il primo imperatore romano?", "options": ["Nerone", "Traiano", "Augusto", "Cesare"], "answer": "Augusto"},
    {"question": "Quale evento storico è associato alla data 1789?", "options": ["La Rivoluzione Francese", "La scoperta dell'America", "La caduta dell'Impero Romano", "L'Unificazione d'Italia"], "answer": "La Rivoluzione Francese"},
    {"question": "Chi ha dipinto la Cappella Sistina?", "options": ["Leonardo da Vinci", "Raffaello", "Michelangelo", "Donatello"], "answer": "Michelangelo"},
    {"question": "Quale città è stata distrutta dall'eruzione del Vesuvio nel 79 d.C.?", "options": ["Roma", "Pompei", "Napoli", "Ercolano"], "answer": "Pompei"},
    {"question": "Chi era il leader dei Nazisti durante la Seconda Guerra Mondiale?", "options": ["Benito Mussolini", "Adolf Hitler", "Winston Churchill", "Franklin D. Roosevelt"], "answer": "Adolf Hitler"},
    {"question": "Chi ha scritto 'Il Principe'?", "options": ["Dante Alighieri", "Machiavelli", "Boccaccio", "Petrarca"], "answer": "Machiavelli"},
    {"question": "In quale anno è stata unificata l'Italia?", "options": ["1848", "1861", "1870", "1859"], "answer": "1861"},
    {"question": "Chi è stato il primo presidente degli Stati Uniti?", "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"], "answer": "George Washington"},
    {"question": "Quale trattato ha posto fine alla Prima Guerra Mondiale?", "options": ["Trattato di Versailles", "Trattato di Parigi", "Trattato di Vienna", "Trattato di Tordesillas"], "answer": "Trattato di Versailles"},
    {"question": "Chi era il faraone dell'Antico Egitto noto per la sua maschera d'oro?", "options": ["Ramses II", "Tutankhamon", "Cleopatra", "Akhenaton"], "answer": "Tutankhamon"},
    {"question": "Qual è stata la causa principale della Guerra Fredda?", "options": ["Conflitto religioso", "Competizione tra USA e URSS", "Colonialismo", "Espansione dell'Impero Britannico"], "answer": "Competizione tra USA e URSS"},
    {"question": "Quale civiltà ha costruito Machu Picchu?", "options": ["Maya", "Inca", "Aztechi", "Olmechi"], "answer": "Inca"},
    {"question": "Chi ha guidato la spedizione che ha circumnavigato il globo per la prima volta?", "options": ["Cristoforo Colombo", "Vasco da Gama", "Ferdinando Magellano", "Amerigo Vespucci"], "answer": "Ferdinando Magellano"},
    {"question": "Chi ha sconfitto Napoleone a Waterloo?", "options": ["Wellington", "Blücher", "Nelson", "Giuseppe Garibaldi"], "answer": "Wellington"},
    {"question": "Chi ha inventato la stampa a caratteri mobili?", "options": ["Galileo Galilei", "Gutenberg", "Leonardo da Vinci", "Isaac Newton"], "answer": "Gutenberg"},
    {"question": "Quale civiltà antica ha costruito le piramidi?", "options": ["Etruschi", "Egizi", "Romani", "Maya"], "answer": "Egizi"},
    {"question": "In quale anno è caduto il Muro di Berlino?", "options": ["1980", "1989", "1991", "1979"], "answer": "1989"},
    {"question": "Chi ha guidato l'Unione Sovietica durante la Seconda Guerra Mondiale?", "options": ["Vladimir Lenin", "Iosif Stalin", "Nikita Krusciov", "Leon Trotsky"], "answer": "Iosif Stalin"},
    {"question": "Quale popolo antico ha fondato Roma, secondo la leggenda?", "options": ["Greci", "Etruschi", "Romani", "Troiani"], "answer": "Troiani"},
    {"question": "In quale anno è caduto l'Impero Romano d'Occidente?", "options": ["476", "410", "1453", "1204"], "answer": "476"},
    {"question": "Chi era il condottiero cartaginese che attraversò le Alpi con gli elefanti?", "options": ["Scipione", "Annibale", "Cesare", "Ciro il Grande"], "answer": "Annibale"},
    {"question": "Quale re inglese ebbe sei mogli?", "options": ["Enrico VIII", "Giorgio III", "Carlo I", "Giacomo II"], "answer": "Enrico VIII"},
    {"question": "Chi ha scritto la 'Divina Commedia'?", "options": ["Dante Alighieri", "Boccaccio", "Petrarca", "Ariosto"], "answer": "Dante Alighieri"},
    {"question": "In quale battaglia Napoleone Bonaparte fu sconfitto definitivamente?", "options": ["Waterloo", "Austerlitz", "Lipsia", "Trafalgar"], "answer": "Waterloo"},
    {"question": "In quale anno è stata firmata la Dichiarazione d'Indipendenza degli Stati Uniti?", "options": ["1776", "1789", "1791", "1812"], "answer": "1776"},
    {"question": "Chi ha scoperto la teoria della relatività?", "options": ["Isaac Newton", "Albert Einstein", "Nikola Tesla", "Galileo Galilei"], "answer": "Albert Einstein"},
    {"question": "Quale civiltà costruì la Grande Muraglia Cinese?", "options": ["Mongoli", "Cinesi", "Persiani", "Romani"], "answer": "Cinesi"},
    {"question": "Chi era il leader della Rivoluzione Russa del 1917?", "options": ["Lenin", "Stalin", "Trotsky", "Kerenskij"], "answer": "Lenin"},
    {"question": "Quale evento ha segnato l'inizio della Seconda Guerra Mondiale?", "options": ["L'invasione della Polonia", "L'attacco a Pearl Harbor", "La marcia su Roma", "La caduta di Berlino"], "answer": "L'invasione della Polonia"}
]
questions_nutrizione = [
    {"question": "Qual è la vitamina che si ottiene principalmente dall'esposizione al sole?", "options": ["Vitamina A", "Vitamina B12", "Vitamina C", "Vitamina D"], "answer": "Vitamina D"},
    {"question": "Quale minerale è essenziale per la formazione delle ossa?", "options": ["Ferro", "Calcio", "Magnesio", "Zinco"], "answer": "Calcio"},
    {"question": "Qual è la principale fonte di energia per il corpo umano?", "options": ["Proteine", "Carboidrati", "Grassi", "Vitamine"], "answer": "Carboidrati"},
    {"question": "Quale vitamina è essenziale per la coagulazione del sangue?", "options": ["Vitamina A", "Vitamina K", "Vitamina E", "Vitamina D"], "answer": "Vitamina K"},
    {"question": "Quale nutriente è essenziale per la crescita e la riparazione dei tessuti?", "options": ["Carboidrati", "Proteine", "Grassi", "Fibre"], "answer": "Proteine"},
    {"question": "Quale vitamina è essenziale per la vista?", "options": ["Vitamina A", "Vitamina B6", "Vitamina C", "Vitamina D"], "answer": "Vitamina A"},
    {"question": "Quale minerale è importante per il trasporto dell'ossigeno nel sangue?", "options": ["Calcio", "Ferro", "Magnesio", "Potassio"], "answer": "Ferro"},
    {"question": "Quale vitamina è essenziale per il sistema immunitario?", "options": ["Vitamina A", "Vitamina B12", "Vitamina C", "Vitamina D"], "answer": "Vitamina C"},
    {"question": "Quale nutriente è essenziale per la produzione di ormoni?", "options": ["Carboidrati", "Proteine", "Grassi", "Fibre"], "answer": "Grassi"},
    {"question": "Quale vitamina è essenziale per la salute della pelle?", "options": ["Vitamina A", "Vitamina B6", "Vitamina C", "Vitamina E"], "answer": "Vitamina E"},
    {"question": "Quale minerale è importante per la funzione muscolare?", "options": ["Calcio", "Ferro", "Magnesio", "Zinco"], "answer": "Magnesio"},
    {"question": "Quale vitamina è essenziale per la sintesi del collagene?", "options": ["Vitamina A", "Vitamina B12", "Vitamina C", "Vitamina D"], "answer": "Vitamina C"},
    {"question": "Quale nutriente è essenziale per la regolazione della temperatura corporea?", "options": ["Carboidrati", "Proteine", "Grassi", "Acqua"], "answer": "Acqua"},
    {"question": "Quale vitamina è essenziale per la produzione di energia?", "options": ["Vitamina A", "Vitamina B12", "Vitamina C", "Vitamina D"], "answer": "Vitamina B12"},
    {"question": "Quale minerale è importante per la salute dei denti?", "options": ["Calcio", "Ferro", "Magnesio", "Fluoro"], "answer": "Fluoro"},
    {"question": "Quale vitamina è essenziale per la funzione cerebrale?", "options": ["Vitamina A", "Vitamina B6", "Vitamina C", "Vitamina D"], "answer": "Vitamina B6"},
    {"question": "Quale nutriente è essenziale per la sintesi delle proteine?", "options": ["Carboidrati", "Proteine", "Grassi", "Aminoacidi"], "answer": "Aminoacidi"},
    {"question": "Quale vitamina è essenziale per la salute del cuore?", "options": ["Vitamina A", "Vitamina B12", "Vitamina C", "Vitamina E"], "answer": "Vitamina E"},
    {"question": "Quale minerale è importante per la regolazione della pressione sanguigna?", "options": ["Calcio", "Ferro", "Magnesio", "Potassio"], "answer": "Potassio"},
    {"question": "Quale vitamina è essenziale per la prevenzione delle malattie croniche?", "options": ["Vitamina A", "Vitamina B12", "Vitamina C", "Vitamina D"], "answer": "Vitamina D"}
]

questions_matematica = [
    {"question": "Qual è il risultato di 5 + 3?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "Qual è il risultato di 12 - 4?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "Qual è il risultato di 3 x 4?", "options": ["10", "11", "12", "13"], "answer": "12"},
    {"question": "Qual è il risultato di 16 ÷ 4?", "options": ["2", "3", "4", "5"], "answer": "4"},
    {"question": "Qual è il valore di π (pi greco) approssimato a due decimali?", "options": ["3.12", "3.14", "3.16", "3.18"], "answer": "3.14"},
    {"question": "Qual è il risultato di 2^3?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "Qual è la radice quadrata di 81?", "options": ["7", "8", "9", "10"], "answer": "9"},
    {"question": "Qual è il risultato di 15 + 6?", "options": ["20", "21", "22", "23"], "answer": "21"},
    {"question": "Qual è il risultato di 25 - 7?", "options": ["16", "17", "18", "19"], "answer": "18"},
    {"question": "Qual è il risultato di 6 x 7?", "options": ["40", "41", "42", "43"], "answer": "42"},
    {"question": "Qual è il risultato di 36 ÷ 6?", "options": ["5", "6", "7", "8"], "answer": "6"},
    {"question": "Qual è il risultato di 4^2?", "options": ["14", "15", "16", "17"], "answer": "16"},
    {"question": "Qual è la radice quadrata di 49?", "options": ["6", "7", "8", "9"], "answer": "7"},
    {"question": "Qual è il risultato di 9 + 8?", "options": ["16", "17", "18", "19"], "answer": "17"},
    {"question": "Qual è il risultato di 20 - 5?", "options": ["14", "15", "16", "17"], "answer": "15"},
    {"question": "Qual è il risultato di 8 x 5?", "options": ["38", "39", "40", "41"], "answer": "40"},
    {"question": "Qual è il risultato di 48 ÷ 8?", "options": ["5", "6", "7", "8"], "answer": "6"},
    {"question": "Qual è il risultato di 3^3?", "options": ["26", "27", "28", "29"], "answer": "27"},
    {"question": "Qual è la radice quadrata di 64?", "options": ["7", "8", "9", "10"], "answer": "8"},
    {"question": "Qual è il risultato di 7 + 6?", "options": ["12", "13", "14", "15"], "answer": "13"}
]

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/start')
def start():
    return render_template('categories.html')

@app.route('/quiz/<category>')
def quiz(category):
    if category == 'capitali':
        session['questions'] = random.sample(questions_capitali, 10)
    elif category == 'sport':
        session['questions'] = random.sample(questions_sport, 10)
    elif category == 'storia':
        session['questions'] = random.sample(questions_storia, 10)
    elif category == 'nutrizione':
        session['questions'] = random.sample(questions_nutrizione, 10)
    elif category == 'matematica':
        session['questions'] = random.sample(questions_matematica, 10)
    else:
        return redirect(url_for('welcome'))

    session['current_question'] = 0
    session['score'] = 0
    session['category'] = category  # Aggiungi la categoria alla sessione
    return redirect(url_for('quiz_question'))

@app.route('/quiz_question', methods=['GET', 'POST'])
def quiz_question():
    current_question = session.get('current_question', 0)
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer:
            session[f'answer_{current_question}'] = answer
            if answer == session['questions'][current_question]['answer']:
                session['score'] += 1
        session['current_question'] += 1
        current_question = session['current_question']
        if current_question >= len(session['questions']):
            return redirect(url_for('result'))

    question = session['questions'][current_question]
    question_number = current_question + 1
    total_questions = len(session['questions'])
    category = session.get('category', 'Quiz')  # Ottieni la categoria dalla sessione
    return render_template('quiz.html', question=question, question_number=question_number, total_questions=total_questions, category=category)

@app.route('/result')
def result():
    if 'questions' not in session:
        return redirect(url_for('start'))
    score = session.get('score', 0)
    total = len(session['questions'])
    results = []
    for i, question in enumerate(session['questions']):
        user_answer = session.get(f'answer_{i}', 'N/A')
        correct_answer = question['answer']
        results.append((i + 1, question['question'], user_answer, correct_answer))
    print("Results:", results)  # Aggiungi questa linea per il debugging
    return render_template('result.html', results=results, score=score, total=total)

@app.route('/check_answers')
def check_answers():
    if 'questions' not in session:
        return redirect(url_for('start'))
    results = []
    for i, question in enumerate(session['questions']):
        correct_answer = question['answer']
        results.append((question['question'], correct_answer))
    return render_template('check_answers.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
