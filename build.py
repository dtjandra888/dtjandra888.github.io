
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

import shutil

template_dir = Path('templates')
static_dir = Path('static')
output_dir = Path('dist')

env = Environment(loader=FileSystemLoader(template_dir))

output_dir.mkdir(parents=True, exist_ok=True)

template = env.get_template('index.html')
html = template.render()

(output_dir / "index.html").write_text(html, encoding="utf-8")
shutil.copytree(static_dir, output_dir / 'static', dirs_exist_ok=True)

# for template in template_dir.rglob('*.html')

print('Finished Rendering')
