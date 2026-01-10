from flask import Flask, request, render_template_string

app = Flask(__name__)

# A simple home page
@app.route('/')
def index():
    return """
        <h1>DAST Practice Lab</h1>
        <p>Search for a product:</p>
        <form action="/search" method="GET">
            <input type="text" name="q">
            <input type="submit" value="Search">
        </form>
    """

# VULNERABILITY: This route reflects the 'q' parameter without sanitization
@app.route('/search')
def search():
    query = request.args.get('q', '')
    template = f"<h2>Results for: {query}</h2><a href='/'>Back</a>"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)