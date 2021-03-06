from flask import render_template, request, Blueprint
from myapp.models import DicePost

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    dice_posts = DicePost.query.order_by(DicePost.date.desc()).paginate(page=page, =4)
    return render_template('index.html', dice_posts=dice_posts)

@core.route('/info')
def info():
    return render_template('info.html')