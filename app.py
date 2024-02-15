from flask import Flask, render_template, abort

projects_names = [
    "Habit Tracking app With Python and MongoDB",
    "Portfolio Website with Typescript and Next js",
    "Blog Website Using Python and MongoDB"

]

projects_details = [
    {
        "num": 0,
        "thumb": "images/finance-tracker-notion-for-business-desktop.png",
        "hero": "images/finance-tracker-notion-for-business-desktop.png",
        "categories": ["Pyhon", "Database"],
        "slug": projects_names[0].replace(" ", "-"),
        "link": "https://github.com/SaadAzil3"
    },
    {
        "num": 1,
        "thumb": "images/Portfolio-Desk.jpg",
        "hero": "images/Portfolio-Desk.jpg",
        "categories": ["Typescript", "Nextjs"],
        "slug": projects_names[1].replace(" ", "-"),
        "link": "https://github.com/SaadAzil3"
    },
    {
        "num": 2,
        "thumb": "images/tumblr_n2lq5lwa8H1sikueao1_1280.jpg",
        "hero": "images/tumblr_n2lq5lwa8H1sikueao1_1280.jpg",
        "categories": ["Pyhon", "Database"],
        "slug": projects_names[2].replace(" ", "-"),
        "link": "https://github.com/SaadAzil3"
    }
]

slug_to_project = {project["slug"]: project for project in projects_details}

app = Flask(__name__)
@app.route("/")
def home():
    
    return render_template("main.html", projects_details=projects_details, projects_names=projects_names)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        print(slug)
        abort(404)
    return render_template(
        f"project_.html",
        project=slug_to_project[slug],
        name=slug.replace("-", " "),
    )

@app.errorhandler(404)
def page_not_found(error):
    return render_template(
        "404.html"
    ), 404