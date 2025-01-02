from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

questions_capitali = [
    {"question": "Qual è la capitale d'Italia?", "options": ["A. Milano", "B. Roma", "C. Napoli", "D. Torino"], "answer": "B"},
    {"question": "Qual è la capitale della Francia?", "options": ["A. Marsiglia", "B. Lione", "C. Parigi", "D. Nizza"], "answer": "C"},
    {"question": "Qual è la capitale della Spagna?", "options": ["A. Barcellona", "B. Valencia", "C. Siviglia", "D. Madrid"], "answer": "D"},
    {"question": "Qual è la capitale della Germania?", "options": ["A. Monaco", "B. Amburgo", "C. Berlino", "D. Francoforte"], "answer": "C"},
    {"question": "Qual è la capitale del Portogallo?", "options": ["A. Porto", "B. Lisbona", "C. Faro", "D. Coimbra"], "answer": "B"},
    {"question": "Qual è la capitale della Grecia?", "options": ["A. Salonicco", "B. Atene", "C. Patrasso", "D. Heraklion"], "answer": "B"},
    {"question": "Qual è la capitale della Russia?", "options": ["A. San Pietroburgo", "B. Mosca", "C. Novosibirsk", "D. Ekaterinburg"], "answer": "B"},
    {"question": "Qual è la capitale del Giappone?", "options": ["A. Osaka", "B. Kyoto", "C. Tokyo", "D. Hiroshima"], "answer": "C"},
    {"question": "Qual è la capitale della Cina?", "options": ["A. Shanghai", "B. Pechino", "C. Guangzhou", "D. Shenzhen"], "answer": "B"},
    {"question": "Qual è la capitale dell'India?", "options": ["A. Mumbai", "B. Nuova Delhi", "C. Bangalore", "D. Chennai"], "answer": "B"},
    {"question": "Qual è la capitale del Brasile?", "options": ["A. Rio de Janeiro", "B. San Paolo", "C. Brasilia", "D. Salvador"], "answer": "C"},
    {"question": "Qual è la capitale dell'Australia?", "options": ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"], "answer": "C"},
    {"question": "Qual è la capitale del Canada?", "options": ["A. Toronto", "B. Vancouver", "C. Ottawa", "D. Montreal"], "answer": "C"},
    {"question": "Qual è la capitale del Messico?", "options": ["A. Guadalajara", "B. Monterrey", "C. Città del Messico", "D. Tijuana"], "answer": "C"},
    {"question": "Qual è la capitale dell'Argentina?", "options": ["A. Buenos Aires", "B. Cordoba", "C. Rosario", "D. Mendoza"], "answer": "A"},
    {"question": "Qual è la capitale del Sudafrica?", "options": ["A. Johannesburg", "B. Città del Capo", "C. Pretoria", "D. Durban"], "answer": "C"},
    {"question": "Qual è la capitale dell'Egitto?", "options": ["A. Alessandria", "B. Il Cairo", "C. Giza", "D. Luxor"], "answer": "B"},
    {"question": "Qual è la capitale della Turchia?", "options": ["A. Istanbul", "B. Ankara", "C. Smirne", "D. Bursa"], "answer": "B"},
    {"question": "Qual è la capitale della Svezia?", "options": ["A. Goteborg", "B. Malmo", "C. Stoccolma", "D. Uppsala"], "answer": "C"},
    {"question": "Qual è la capitale della Norvegia?", "options": ["A. Bergen", "B. Trondheim", "C. Oslo", "D. Stavanger"], "answer": "C"}
]

questions_sport = [
    {"question": "Qual è lo sport più praticato al mondo?", "options": ["A. Calcio", "B. Basket", "C. Tennis", "D. Cricket"], "answer": "A"},
    {"question": "In quale anno si sono tenuti i primi Giochi Olimpici moderni?", "options": ["A. 1896", "B. 1900", "C. 1924", "D. 1936"], "answer": "A"},
    {"question": "Chi ha vinto il maggior numero di titoli del Grande Slam nel tennis?", "options": ["A. Roger Federer", "B. Rafael Nadal", "C. Novak Djokovic", "D. Pete Sampras"], "answer": "C"},
    {"question": "Qual è il paese con il maggior numero di Coppe del Mondo di calcio?", "options": ["A. Brasile", "B. Germania", "C. Italia", "D. Argentina"], "answer": "A"},
    {"question": "Qual è il record mondiale dei 100 metri piani?", "options": ["A. 9.58 secondi", "B. 9.63 secondi", "C. 9.69 secondi", "D. 9.72 secondi"], "answer": "A"},
    {"question": "Chi ha vinto il maggior numero di Tour de France?", "options": ["A. Lance Armstrong", "B. Eddy Merckx", "C. Bernard Hinault", "D. Miguel Indurain"], "answer": "B"},
    {"question": "Qual è il paese con il maggior numero di medaglie olimpiche?", "options": ["A. Stati Uniti", "B. Russia", "C. Cina", "D. Germania"], "answer": "A"},
    {"question": "Qual è il record mondiale del salto in lungo?", "options": ["A. 8.90 metri", "B. 8.95 metri", "C. 8.99 metri", "D. 9.00 metri"], "answer": "B"},
    {"question": "Chi ha vinto il maggior numero di titoli NBA?", "options": ["A. Michael Jordan", "B. LeBron James", "C. Bill Russell", "D. Kareem Abdul-Jabbar"], "answer": "C"},
    {"question": "Qual è il record mondiale del lancio del giavellotto?", "options": ["A. 98.48 metri", "B. 98.52 metri", "C. 98.58 metri", "D. 98.62 metri"], "answer": "C"},
    {"question": "Chi ha vinto il maggior numero di titoli di Formula 1?", "options": ["A. Michael Schumacher", "B. Lewis Hamilton", "C. Ayrton Senna", "D. Alain Prost"], "answer": "A"},
    {"question": "Qual è il record mondiale dei 200 metri piani?", "options": ["A. 19.19 secondi", "B. 19.26 secondi", "C. 19.32 secondi", "D. 19.40 secondi"], "answer": "A"},
    {"question": "Chi ha vinto il maggior numero di titoli di Wimbledon?", "options": ["A. Roger Federer", "B. Pete Sampras", "C. Novak Djokovic", "D. Rafael Nadal"], "answer": "A"},
    {"question": "Qual è il record mondiale del salto con l'asta?", "options": ["A. 6.14 metri", "B. 6.16 metri", "C. 6.18 metri", "D. 6.20 metri"], "answer": "D"},
    {"question": "Chi ha vinto il maggior numero di titoli di golf?", "options": ["A. Jack Nicklaus", "B. Tiger Woods", "C. Arnold Palmer", "D. Gary Player"], "answer": "A"},
    {"question": "Qual è il record mondiale dei 400 metri piani?", "options": ["A. 43.03 secondi", "B. 43.18 secondi", "C. 43.29 secondi", "D. 43.45 secondi"], "answer": "A"},
    {"question": "Chi ha vinto il maggior numero di titoli di boxe?", "options": ["A. Muhammad Ali", "B. Mike Tyson", "C. Floyd Mayweather", "D. Manny Pacquiao"], "answer": "C"},
    {"question": "Qual è il record mondiale del sollevamento pesi?", "options": ["A. 263 kg", "B. 266 kg", "C. 270 kg", "D. 273 kg"], "answer": "D"},
    {"question": "Chi ha vinto il maggior numero di titoli di ciclismo su pista?", "options": ["A. Chris Hoy", "B. Bradley Wiggins", "C. Mark Cavendish", "D. Jason Kenny"], "answer": "D"},
    {"question": "Qual è il record mondiale del salto triplo?", "options": ["A. 18.29 metri", "B. 18.35 metri", "C. 18.39 metri", "D. 18.43 metri"], "answer": "A"}
]

questions_storia = [
    {"question": "In che anno è caduto il Muro di Berlino?", "options": ["A. 1987", "B. 1989", "C. 1991", "D. 1993"], "answer": "B"},
    {"question": "Chi era il presidente degli Stati Uniti durante la Guerra Civile?", "options": ["A. George Washington", "B. Thomas Jefferson", "C. Abraham Lincoln", "D. Theodore Roosevelt"], "answer": "C"},
    {"question": "Quale evento ha scatenato la Prima Guerra Mondiale?", "options": ["A. L'assassinio dell'arciduca Francesco Ferdinando", "B. L'invasione della Polonia", "C. La Rivoluzione Russa", "D. La Conferenza di Versailles"], "answer": "A"},
    {"question": "Chi ha scoperto l'America?", "options": ["A. Cristoforo Colombo", "B. Amerigo Vespucci", "C. Ferdinando Magellano", "D. Vasco da Gama"], "answer": "A"},
    {"question": "In che anno è iniziata la Seconda Guerra Mondiale?", "options": ["A. 1937", "B. 1938", "C. 1939", "D. 1940"], "answer": "C"},
    {"question": "Chi era il primo imperatore di Roma?", "options": ["A. Giulio Cesare", "B. Augusto", "C. Nerone", "D. Traiano"], "answer": "B"},
    {"question": "Quale rivoluzione ha portato alla caduta della monarchia francese?", "options": ["A. Rivoluzione Americana", "B. Rivoluzione Francese", "C. Rivoluzione Russa", "D. Rivoluzione Industriale"], "answer": "B"},
    {"question": "Chi ha scritto la Dichiarazione di Indipendenza degli Stati Uniti?", "options": ["A. George Washington", "B. Benjamin Franklin", "C. Thomas Jefferson", "D. John Adams"], "answer": "C"},
    {"question": "In che anno è stata fondata l'ONU?", "options": ["A. 1943", "B. 1945", "C. 1947", "D. 1949"], "answer": "B"},
    {"question": "Chi era il leader dell'Unione Sovietica durante la Seconda Guerra Mondiale?", "options": ["A. Lenin", "B. Stalin", "C. Krusciov", "D. Breznev"], "answer": "B"},
    {"question": "Quale paese ha costruito la Grande Muraglia?", "options": ["A. Giappone", "B. Corea", "C. Cina", "D. Mongolia"], "answer": "C"},
    {"question": "Chi era il re d'Inghilterra durante la Guerra dei Cent'anni?", "options": ["A. Enrico V", "B. Edoardo III", "C. Riccardo II", "D. Giovanni Senza Terra"], "answer": "B"},
    {"question": "Quale evento ha segnato l'inizio del Medioevo?", "options": ["A. Caduta di Roma", "B. Invasione dei Normanni", "C. Battaglia di Hastings", "D. Scoperta dell'America"], "answer": "A"},
    {"question": "Chi ha guidato la Rivoluzione Russa del 1917?", "options": ["A. Lenin", "B. Trotsky", "C. Stalin", "D. Kerensky"], "answer": "A"},
    {"question": "In che anno è stata firmata la Magna Carta?", "options": ["A. 1215", "B. 1225", "C. 1235", "D. 1245"], "answer": "A"},
    {"question": "Chi era il presidente degli Stati Uniti durante la Grande Depressione?", "options": ["A. Herbert Hoover", "B. Franklin D. Roosevelt", "C. Harry S. Truman", "D. Dwight D. Eisenhower"], "answer": "B"},
    {"question": "Quale paese ha lanciato il primo satellite artificiale nello spazio?", "options": ["A. Stati Uniti", "B. Unione Sovietica", "C. Cina", "D. Giappone"], "answer": "B"},
    {"question": "Chi era il leader della Germania nazista durante la Seconda Guerra Mondiale?", "options": ["A. Adolf Hitler", "B. Heinrich Himmler", "C. Joseph Goebbels", "D. Hermann Göring"], "answer": "A"},
    {"question": "Quale evento ha segnato la fine della Seconda Guerra Mondiale?", "options": ["A. Battaglia di Stalingrado", "B. Sbarco in Normandia", "C. Bombardamento di Hiroshima e Nagasaki", "D. Conferenza di Yalta"], "answer": "C"},
    {"question": "Chi era il primo ministro britannico durante la Seconda Guerra Mondiale?", "options": ["A. Winston Churchill", "B. Neville Chamberlain", "C. Clement Attlee", "D. Anthony Eden"], "answer": "A"}
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
        session['questions'] = random.sample(questions_capitali, len(questions_capitali))
    elif category == 'sport':
        session['questions'] = random.sample(questions_sport, len(questions_sport))
    elif category == 'storia':
        session['questions'] = random.sample(questions_storia, len(questions_storia))
    else:
        return redirect(url_for('welcome'))

    session['current_question'] = 0
    session['score'] = 0
    return redirect(url_for('quiz_question'))

@app.route('/quiz_question', methods=['GET', 'POST'])
def quiz_question():
    current_question = session.get('current_question', 0)
    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer and answer == session['questions'][current_question]['answer']:
            session['score'] += 1
        session['current_question'] += 1
        current_question = session['current_question']
        if current_question >= len(session['questions']):
            return redirect(url_for('result'))

    question = session['questions'][current_question]
    question_number = current_question + 1
    total_questions = len(session['questions'])
    return render_template('quiz.html', question=question, q=current_question, question_number=question_number, total_questions=total_questions)

@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(session['questions'])
    return render_template('result.html', score=score, total=total)

if __name__ == "__main__":
    app.run(debug=True)
