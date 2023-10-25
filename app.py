from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')



# sınav soruları ve doğru cevapları
questions = [
    {
        'question': 'Python ile yapay zeka geliştirme sürecinde hangi kütüphane en yaygın olarak kullanılır?',
        'options': ['TensorFlow', 'NumPy', 'BeautifulSoup', 'Matplotlib'],
        'answer': 0
    },
    {
        'question': 'Hangi Python kütüphanesi, ses işleme ve konuşma tanıma gibi ses tabanlı yapay zeka uygulamaları geliştirmek için kullanılır?',
        'options': ['librosa', 'NLTK',  'OpenCV', 'PyTorch'],
        'answer': 0
    },
    {
        'question': 'Bir yapay sinir ağı modelini eğitirken, hangi işlem sırasında modelin tahminlerini gerçek etiketlerle karşılaştırıp hatayı hesaplarız?',
        'options': ['Doğrulama (Validation)', 'Aktivasyon (Activation)',  'İnferans (Inference)', 'Derleme (Compilation)'],
        'answer': 2
    }
]

# en yüksek puan değişkeni
highest_score = 0


@app.route('/')
def home():
    return render_template('index.html', questions=questions, highest_score=highest_score)

@app.route('/quiz', methods=['POST'])
def quiz():
    # kullanıcıdan cevap alma
    user_answers = []
    for i in range(len(questions)):
        selected_option = request.form.get(f'q{i}')
        if selected_option is not None:
            user_answers.append(int(selected_option))
        else:
            user_answers.append(-1)

    # skor hesaplama ve en yüksek skoru güncelleme
    score = 0
    for i in range(len(questions)):
        if user_answers[i] == questions[i]['answer']:
            score += 1

    global highest_score
    if score > highest_score:
        highest_score = score


    return render_template('index.html', questions=questions, highest_score=highest_score, score=score)

""" @app.route('/quiz', methods=['POST'])
def quiz():
    # kullanıcıdan cevap alma
    user_answers = []
    for i in range(len(questions)):
        selected_options = request.form.getlist(f'q{i}')
        user_answers.append([int(option) for option in selected_options])

    # skor hesaplama ve en yüksek skoru yazma
    score = 0
    for i in range(len(questions)):
        is_correct = all(option == questions[i]['answer'] for option in user_answers[i])
        if is_correct:
            score += 1

    global highest_score
    if score > highest_score:
        highest_score = score

    return render_template('index.html', questions=questions, highest_score=highest_score, score=score) """


if __name__ == '__main__':
    app.run()
