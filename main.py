from flask import Flask, render_template, request, redirect

from scrape_song import scrape_song
from scraping import scrap_lyric


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search_input = ''
    if request.method == 'POST':
      search_input = request.form.get('search_input')

    data = scrap_lyric(search_input)    #{'artist': artist, 'title': title, 'description': description, 'lyric': lyric}

    return render_template('home.html', data=data)
    
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 