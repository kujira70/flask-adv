from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

# Load the data from the Excel file
df = pd.read_excel("story_data.xlsx", index_col="node_key")

@app.route('/')
def index():
    return redirect(url_for('story', node_key='start'))

@app.route('/story/<node_key>', methods=['GET', 'POST'])
def story(node_key):
    if request.method == 'POST':
        choice = request.form.get('choice')
        if choice == '0':
            node_key = df.loc[node_key, 'next_q']
        elif choice == '1':
            node_key = df.loc[node_key, 'next_w']
        elif choice == '2':
            node_key = df.loc[node_key, 'next_e']
        elif choice == '3':
            node_key = df.loc[node_key, 'next_r']

    story_text = df.loc[node_key, 'text']
    choices = {
        'q': df.loc[node_key, 'choice_q'],
        'w': df.loc[node_key, 'choice_w'],
        'e': df.loc[node_key, 'choice_e'],
        'r': df.loc[node_key, 'choice_r']
    }
    return render_template('story.html', story=story_text, choices=choices)

if __name__ == '__main__':
    app.run(debug=True)
