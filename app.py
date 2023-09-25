import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load story data from Excel
df = pd.read_excel("story_data.xlsx")
story_data = {}
for _, row in df.iterrows():
    node_key = row['node_key']
    story_data[node_key] = {
        "text": row['text'],
        "choices": {
            "q": {"text": row['choice_q'], "next": row['next_q']},
            "w": {"text": row['choice_w'], "next": row['next_w']},
            "e": {"text": row['choice_e'], "next": row['next_e']},
            "r": {"text": row['choice_r'], "next": row['next_r']}
        }
    }

@app.route('/')
def index():
    node = story_data["start"]
    return render_template('story.html', node=node)

if __name__ == '__main__':
    app.run(debug=True)
