### Step #8

Rendering templates, using Jinja2.

Flask will look for templates in the templates folder. If your application is a module, this folder is next to that module, if it's a package it's actually inside your package.

**Module**:

```
/application.py
/templates
  /hello.html
```

**Package**:

```
/application
  /__init__.py
  /templates
    /hello.html
```
