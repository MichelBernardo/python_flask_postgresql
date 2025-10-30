from src import create_app
import os


# Loads the environment configuration.
env = os.getenv('FLASK_ENV', 'development')

# Creates the Flask application instance using the factory.
app = create_app(env)

if __name__ == '__main__':
    # Retrieves the application configuration port.
    port = app.config.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)