from app import create_app

app = create_app()

# This is required for Vercel to find the app
from flask import Flask
if __name__ == "__main__":
    app.run()
