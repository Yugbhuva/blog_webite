from flask_blog.app import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)