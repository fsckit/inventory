import os

def mustache(request):
  # Load all templates
  templates = []
  for path, dirs, files in os.walk('app/templates/mustache'):
    for f in files:
      if f.endswith('.html'):
        filepath = os.path.join(path, f)
        templates.append({ 'id': os.path.splitext(f)[0], 'contents': open(filepath, 'r').read() })
  return { 'templates': templates }
