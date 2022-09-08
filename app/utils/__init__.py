def cleanup(db, app):
    """
    This method cleans up the session object and closes the connection pool using the dispose
    method.
    """
    db.session.close()
    engine_container = db.get_engine(app)
    engine_container.dispose()
