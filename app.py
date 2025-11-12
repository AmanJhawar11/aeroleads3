import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import google.generativeai as genai
from perplexity import Perplexity



app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


GOOGLE_API_KEY = "" 
PERPLEXITY_API_KEY = ""

# 2. DATABASE MODEL 

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Article {self.title}>'

# 3. AI HELPER FUNCTION 

def generate_article_content(topic):
    prompt = f"""
    You are an expert blog post writer. 
    Your task is to write a full, high-quality article on the following topic: "{topic}".
    Please format your response in simple HTML.
    - Use <h2> for subheadings.
    - Use <p> for paragraphs.
    - Use <ul>, <ol>, and <li> for lists.
    - Use <strong> for bold text.
    - Do NOT include a <h1> title, as I will add that myself.
    - Just write the body of the article.
    """
    
    try:
        # Use the corrected model name
        model = genai.GenerativeModel('gemini-1.0-pro') 
        response = model.generate_content(prompt)
        content = response.text.replace("```html", "").replace("```", "").strip()
        return content
    except Exception as e:
        print(f"Error calling Gemini AI: {e}")
        return "<p><strong>Error: Could not generate article.</strong> Please check your API key and try again.</p>"

# 4. FLASK ROUTES 

@app.route('/')
@app.route('/blog')
def blog_home():
    """
    Shows the main blog page with all articles.
    This page NOW includes the forms.
    """
    articles = Article.query.order_by(Article.id.desc()).all()
    return render_template('blog.html', title='Blog & Admin', articles=articles)

@app.route('/article/<int:article_id>')
def article_detail(article_id):
    """Shows one specific article."""
    article = Article.query.get_or_404(article_id)
    return render_template('article.html', title=article.title, article=article)



@app.route('/generate-ai-post', methods=['POST'])
def generate_ai_post():
    """Handles the AI generator form."""
    if request.method == 'POST':
        topic = request.form['topic']
        print(f"AI is generating an article about: {topic}...")
        
        ai_content = generate_article_content(topic)
        
        new_article = Article(title=topic, content=ai_content)
        db.session.add(new_article)
        db.session.commit()
        
        print("...Article saved to database!")
        # Send the user back to the blog home
        return redirect(url_for('blog_home'))

@app.route('/create-manual-post', methods=['POST'])
def create_manual_post():
    """Handles the manual upload form."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        new_article = Article(title=title, content=content)
        db.session.add(new_article)
        db.session.commit()
        
        # Send the user back to the blog home
        return redirect(url_for('blog_home'))

# --- 5. RUN THE APP ---
if __name__ == '__main__':
    with app.app_context():
        # This creates the 'blog.db' file if it doesn't exist
        db.create_all()
    
    # Starts your web server
    app.run(debug=True, port=5000)