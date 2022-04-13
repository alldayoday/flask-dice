from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import DicePost
from myapp.dice_posts.forms import DicePostForm

dice_posts = Blueprint('dice_posts', __name__)

@dice_posts.route('/create', methods=['GET', 'POST'])
@login_required
def create_post():
    form = DicePostForm()
    if form.validate_on_submit():
        dice_post = DicePost(link=form.link.data, user_id=current_user.id)
        db.session.add(dice_post)
        db.session.commit()
        flash('Dice Post Created')
        print('Dice post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)



@dice_posts.route('/<int:dice_post_id>')
def dice_post(dice_post_id):
    dice_post = DicePost.query.get_or_404(dice_post_id) 
    return render_template('dice_post.html', link=dice_post.link, date=dice_post.date, post=dice_post)

@dice_posts.route('/<int:dice_post_id>/update',methods=['GET','POST'])
@login_required
def update(dice_post_id):
    dice_post = DicePost.query.get_or_404(dice_post_id)

    if dice_post.author != current_user:
        abort(403)

    form = DicePostForm()

    if form.validate_on_submit():
        dice_post.link = form.link.data
        db.session.commit()
        flash('Dice Post Updated')
        return redirect(url_for('core.index'))

    elif request.method == 'GET':
        form.link.data = dice_post.link

    return render_template('create_post.html',title='Updating',form=form)

@dice_posts.route('/<int:dice_post_id>/delete',methods=['GET','POST'])
@login_required
def delete_post(dice_post_id):

    dice_post = DicePost.query.get_or_404(dice_post_id)
    if dice_post.author != current_user:
        abort(403)

    db.session.delete(dice_post)
    db.session.commit()
    flash('Dice Post Deleted')
    return redirect(url_for('core.index'))