from templates import app

#Load this config object for development mode
app.config.from_object('configurations.DevelopmentConfig')

#Load this config object for production mode
# app.config.from_object('configurations.ProductionConfig')

#Load this config object for production mode
# app.config.from_object('configurations.BaseConfig(')

app.run()