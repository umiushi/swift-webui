import importlib
import pkgutil

from flask import Blueprint


def register_blueprints(app, package_name, package_path):
    """
    Register all Blueprint found in the modules for the specified package.

    :param app:
        The Flask application.
    :param package_name:
        The package name.
    :param package_path:
        The package path.
    """
    rv = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        m = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(m):
            item = getattr(m, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            rv.append(item)
    return rv
