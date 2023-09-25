from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the story data from the Excel file
df = pd.read_excel("story_data.xlsx")

@app.route('/')
def start():
    return story("start")

@app.route('/<node_key>')
def story(node_key):
    row_num = df[df['node_key'] == node_key].index[0]
    story_text = df.iloc[row_num]['text']
    choices = {
        'Q': df.iloc[row_num]['choice_q'],
        'W': df.iloc[row_num]['choice_w'],
        'E': df.iloc[row_num]['choice_e'],
        'R': df.iloc[row_num]['choice_r']
    }
    next_nodes = {
        'Q': df.iloc[row_num]['next_q'],
        'W': df.iloc[row_num]['next_w'],
        'E': df.iloc[row_num]['next_e'],
        'R': df.iloc[row_num]['next_r']
    }
    return render_template("story.html", story_text=story_text, choices=choices, next_nodes=next_nodes)

if __name__ == "__main__":
    app.run(debug=True)
