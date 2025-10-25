
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

import markdown
import shutil

if __name__ == '__main__':
    template_dir = Path('templates')
    static_dir = Path('static')
    posts_dir = Path('posts')
    output_dir = Path('dist')

    env = Environment(loader=FileSystemLoader(template_dir))

    output_dir.mkdir(parents=True, exist_ok=True)

    # Copy static assets needed for site
    shutil.copytree(static_dir, output_dir / 'static', dirs_exist_ok=True)

    # Render index.html
    template = env.get_template('index.html')
    html = template.render()
    (output_dir / "index.html").write_text(html, encoding="utf-8")

    print('Finished Rendering index.html')

    # Making blog directory
    blog_dir = (output_dir / 'blog')
    blog_dir.mkdir(parents=True, exist_ok=True)

    # Iterate over all md docs and write all post pages
    # TODO: only render newly created files
    posts = []
    for post in posts_dir.glob('*.md'):

        post_name = post.stem
        post_dir = blog_dir / f'{post_name}.html'

        # Render markdown file into html
        content = markdown.markdown(post.read_text(
            encoding='utf-8'), extensions=['toc', 'codehilite', 'extra'])

        post_template = env.get_template('post.html')
        post_html = post_template.render(
            title=post_name.replace('-', ' ').title(),
            content=content,
        )

        # Save post output
        post_dir.write_text(post_html, encoding='utf-8')

        # Keep track of post metadata for blog listing
        posts.append({
            'title': post_name.replace('-', ' ').title(),
            'url': f'blog/{post_name}.html',
        })

    print('Finished Rendering posts')

    # Render blog page
    blog_template = env.get_template('blog.html')
    blog_html = blog_template.render(posts=posts)
    (output_dir / 'blog.html').write_text(blog_html, encoding='utf-8')

    print('Finished Rendering')
