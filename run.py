

# from flask import Flask
# from app.extensions import db
# from app.app_manager import AppManager
# from app.routes.authorizedRoutes.auth_routes import auth_bp
# from app.routes.fileRoutes.file_routes import file_bp
# from app.routes.mainRoutes.main_routes import user_routes

# def create_app():
#     app = Flask(__name__)

#     # Load the configuration from your Config class
#     app.config.from_object('app.config.Config')

#     # Initialize extensions like db (SQLAlchemy)
#     db.init_app(app)
#     from flask_smorest import Api

    


#     # Initialize the Api object from flask-smorest
#     api = Api(app, 
#               spec_kwargs={
#                   "components": {
#                       "securitySchemes": {
#                           "bearerAuth": {
#                               "type": "http",
#                               "scheme": "bearer",
#                               "bearerFormat": "JWT"
#                           }
#                       }
#                   },
#                   "security": [{"bearerAuth": []}]
#               })

#     # Set API title, version, and description
#     api.spec.title = "Your API"
#     api.spec.version = "1.0"
#     api.spec.description = "Your API description"

#     # Register your blueprints (routes)
#     api.register_blueprint(auth_bp)
#     api.register_blueprint(file_bp)
#     api.register_blueprint(user_routes)

#     # Optional: Define additional routes directly in the app
#     @app.route('/')
#     def index():
#         return "Welcome to the Flask API"

#     return app


# # if __name__ == '__main__':
# #     app = create_app()
    
# #     # Initialize database and create tables if necessary
# #     with app.app_context():
# #         try:
# #             app_manager = AppManager()
# #             app_manager._create_tables()
# #             app.logger.debug("Tables created successfully.")
# #         except Exception as e:
# #             app.logger.error(f"Error creating tables: {e}")

# #     # Run the Flask application with the specified host and port
# #     app.run(host='13.202.31.71', port=8080, debug=True)
# #     # app.run(host='0.0.0.0', port=8080, debug=True)

# import logging

# if __name__ == '__main__':
#     app = create_app()
    
#     # Enable detailed logging
#     logging.basicConfig(level=logging.DEBUG)
    
#     # Initialize database and create tables if necessary
#     with app.app_context():
#         try:
#             app_manager = AppManager()
#             app_manager._create_tables()
#             app.logger.debug("Tables created successfully.")
#         except Exception as e:
#             app.logger.error(f"Error creating tables: {e}")

#     app.logger.debug("Starting Flask application...")
    
#     # Run the Flask application
#     try:
#         app.run(host='13.202.31.71', port=8080, debug=True)
#     except Exception as e:
#         app.logger.error(f"Error running Flask app: {e}")




import logging
from flask import Flask
from app.extensions import db, jwt
from app.app_manager import AppManager
from flask_jwt_extended import JWTManager
from app.routes.authorizedRoutes.auth_routes import auth_bp
from app.routes.fileRoutes.file_routes import file_bp
from app.routes.mainRoutes.main_routes import user_routes
from app.routes.get_elements.get_update_profile import get_update_roots
from app.routes.document_get_routes.documet_get_list_routes import document_list_routes
from app.routes.document_delete_routes.document_routes_by_id import document_delete_routes
from app.routes.document_filtered_list.filtered_document_list import document_filtered_routes
from app.routes.get_all_user_routes.get_alluser import usergetall_blueprint
from app.routes.document_routes_get_extract.extract_get_routes import document_extract_get_bp
from app.routes.extract_updates_routes.update_extract_routes import extract_update_bp
from app.routes.download_api_routes.download_routes import document_download_bp
from app.routes.oauth_google_routes.oauth_google_login_routes import google_auth_bp
from flask_smorest import Api
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app, resources={r"/*": {"origins": "*"}}) 
    # Initialize extensions like db (SQLAlchemy)
    db.init_app(app)
    jwt.init_app(app)
   

    # Initialize the Api object from flask-smorest
    api = Api(app, 
              spec_kwargs={
                  "components": {
                      "securitySchemes": {
                          "bearerAuth": {
                              "type": "http",
                              "scheme": "bearer",
                              "bearerFormat": "JWT"
                          }
                      }
                  },
                  "security": [{"bearerAuth": []}]
              })
    api.spec.title = "Your API"
    api.spec.version = "1.0"
    api.spec.description = "Your API description"

    # Register your blueprints (routes)
    api.register_blueprint(auth_bp)
    api.register_blueprint(file_bp)
    api.register_blueprint(user_routes)
    api.register_blueprint(get_update_roots)
    api.register_blueprint(document_list_routes)
    api.register_blueprint(document_delete_routes)
    api.register_blueprint(document_filtered_routes)
    api.register_blueprint(usergetall_blueprint)
    api.register_blueprint(document_extract_get_bp)
    api.register_blueprint(extract_update_bp)
    api.register_blueprint(document_download_bp)
    api.register_blueprint(google_auth_bp)

    
    

    @app.route('/')
    def index():
        return "Welcome to the Flask API"

    return app


app = create_app()
logging.basicConfig(level=logging.DEBUG)

# Initialize database and create tables if necessary
with app.app_context():
    try:
        app_manager = AppManager()
        app_manager._create_tables()
        app.logger.debug("Tables created successfully.")
    except Exception as e:
        app.logger.error(f"Error creating tables: {e}")

app.logger.debug("Starting Flask application...")

try:
    app.run(host='0.0.0.0', port=8086, debug=True)
except Exception as e:
    app.logger.error(f"Error running Flask app: {e}")


