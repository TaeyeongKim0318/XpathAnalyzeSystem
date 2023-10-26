from flask import Flask, render_template, request
import XpathRecommendSystem  # XpathRecommendSystem.py 모듈을 import

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        xpath_data = request.form.get('xpath_data')
        xpath_list = xpath_data.split('\n')
        recommended_xpaths = XpathRecommendSystem.recommend_patterns(xpath_list)
        return render_template('result.html', xpath_data=xpath_list, recommended_xpaths=recommended_xpaths)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
